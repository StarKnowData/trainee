"""Sudoku.py

PADS-based command-line application for generating and solving Sudoku puzzles.
These puzzles are given as a 9x9 grid of cells, some of which are filled with
digits in the range 1-9.  The task is to fill the remaining cells in such a
way that each row of the grid, each column of the grid, and each of nine 3x3
squares into which the grid is partitioned, all have one copy of each of the
nine digits.

A proper Sudoku puzzle must have a unique solution, and it should be possible
to reach that solution by a sequence of logical deductions without trial and
error.  To the extent possible, we strive to keep the same ethic in our
automated solver, by mimicking human rule-based reasoning, rather than
resorting to brute force backtracking search.

D. Eppstein, July 2005.
"""

import random
import sys
from optparse import OptionParser
from BipartiteMatching import imperfections
from StrongConnectivity import StronglyConnectedComponents
from Repetitivity import NonrepetitiveGraph
from Wrap import wrap
from Not import Not
from TwoSatisfiability import Forced
from SVG import SVG

class BadSudoku(Exception): pass
    # raised when we discover that a puzzle has no solutions

# ======================================================================
#   Bitmaps and patterns
# ======================================================================

digits = range(1,10)

class group:
    def __init__(self, i, j, x, y, name):
        mask = 0
        h,k = [q for q in range(4) if q != i and q != j]
        for w in range(3):
            for z in range(3):
                mask |= 1 << (x*3**i + y*3**j + w*3**h + z*3**k)
        self.mask = mask
        self.pos = [None]*9
        self.name = "%s %d" % (name,x+3*y+1)

cols = [group(0,1,x,y,"column") for x in range(3) for y in range(3)]
rows = [group(2,3,x,y,"row") for x in range(3) for y in range(3)]
sqrs = [group(1,3,x,y,"square") for x in range(3) for y in range(3)]
groups = sqrs+rows+cols

neighbors = [0]*81
for i in range(81):
    b = 1<<i
    for g in groups:
        if g.mask & b:
            neighbors[i] |= (g.mask &~ b)

unmask = {}
for i in range(81):
    unmask[1<<i] = i

alignments = {}
for s in sqrs:
    for g in rows+cols:
        m = s.mask&g.mask
        if m:
            alignments[m] = (s,g)
            b1 = m &~ (m-1)
            m &=~ b1
            b2 = m &~ (m-1)
            b3 = m &~ b2
            alignments[b1|b2]=alignments[b1|b3]=alignments[b2|b3]=(s,g)   

triads = []
for square in sqrs:
    for group in rows+cols:
        triads.append((square.mask & group.mask,square,group))

# pairs of rows and columns that cross the same squares
nearby = {}
for g in rows+cols:
    nearby[g] = []
for r1 in rows:
    for s in sqrs:
        if r1.mask & s.mask != 0:
            for r2 in rows:
                if r1 != r2 and r2.mask & s.mask != 0:
                    nearby[r1].append(r2)
            break
for c1 in cols:
    for s in sqrs:
        if c1.mask & s.mask != 0:
            for c2 in cols:
                if c1.mask < c2.mask and c2.mask & s.mask != 0:
                    nearby[c1].append(c2)
            break

FullPlacementGraph = {}

def searchPlacements(node,census):
    if node in FullPlacementGraph:
        return
    FullPlacementGraph[node] = {}
    for i in range(9):
        b = 1<<i
        if node & b:
            continue    # row already used, can't use it again
        if census[i//3] > min(census):
            continue    # block already filled, can't use this row now
        FullPlacementGraph[node][node|b] = 1<<(9*i+sum(census))   # found edge
        census[i//3] += 1
        searchPlacements(node|b,census)   # recurse
        census[i//3] -= 1

searchPlacements(0,[0,0,0])



# ======================================================================
#   Human-readable names for puzzle cells
# ======================================================================

cellnames = [None]*81
for row in range(9):
    for col in range(9):
        cellnames[row*9+col] = ''.join(['R',str(row+1),'C',str(col+1)])

def andlist(list,conjunction="and"):
    """Turn list of strings into English text."""
    if len(list) == 0:
        return "(empty list!)"
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return (' '+conjunction+' ').join(list)
    else:
        return ', '.join(list[:-1]+[conjunction+' '+list[-1]])

def namecells(mask,conjunction="and"):
    """English string describing a sequence of cells."""
    names = []
    while mask:
        bit = mask &~ (mask - 1)
        names.append(cellnames[unmask[bit]])
        mask &=~ bit
    return andlist(names,conjunction)

def pathname(cells):
    return '-'.join([cellnames[c] for c in cells])

def plural(howmany,objectname):
    if howmany == 1:
        return objectname
    else:
        return "%d %ss" % (howmany,objectname)

# ======================================================================
#   State for puzzle solver
# ======================================================================

class Sudoku:
    """
    Data structure for storing and manipulating Sudoku puzzles.
    The actual rules for solving the puzzles are implemented
    separately from this class.
    """

    def __init__(self,initial_placements = None):
        """
        Initialize a new Sudoku grid.
        
        If an argument is given, it should either be a sequence of 81
        digits 0-9 (0 meaning a not-yet-filled cell), or a sequence
        of (digit,cell) pairs.
        
        The main state we use for the solver is an array contents[]
        of 81 cells containing digits 0-9 (0 for an unfilled cell)
        and an array locations[] indexed by the digits 1-9, containing
        bitmasks of the cells still available to each digit.
        
        We also store additional fields:

        - progress is a boolean, set whenever one of our methods
          changes the state of the puzzle, and used by step() to tell
          whether one of its rules fired.
          
        - rules_used is a set of the rule names that have made progress.
        
        - pairs is a dictionary mapping bitmasks of pairs of cells to
          lists of digits that must be located in that pair, as set up
          by the pair rule and used by other later rules.
          
        - bilocation is a NonrepetitiveGraph representing paths and
          cycles among bilocated digits, as constructed by the bilocal
          rule and used by the repeat and conflict rules.
        
        - bivalues is a NonrepetitiveGraph representing paths and
          cycles among bivalued cells, as constructed by the bivalue
          rule and used by the repeat and conflict rules.
          
        - otherbv maps pairs (cell,digit) in the bivalue graph to the
          other digit available at the same cell
        
        - logstream is a stream on which to log verbose descriptions
          of the steps made by the solver (typically sys.stderr), or
          None if verbose descriptions are not to be logged.
        
        - steps is used to count how many solver passes we've made so far.
        
        - original_cells is a bitmask of cells that were originally nonempty.
        
        - assume_unique should be set true to enable solution rules
          based on the assumption that there exists a unique solution
          
        - twosat should be set true to enable a 2SAT-based solution rule
        """
        self.contents = [0]*81
        self.locations = [None]+[(1<<81)-1]*9
        self.rules_used = set()
        self.progress = False
        self.pairs = None
        self.bilocation = None
        self.logstream = False
        self.steps = 0
        self.original_cells = 0
        self.assume_unique = False
        self.twosat = False

        if initial_placements:
            cell = 0
            for item in initial_placements:
                try:
                    digit = int(item)
                except TypeError:
                    digit,cell = item
                if digit:
                    self.place(digit,cell)
                    self.original_cells |= 1 << cell
                cell += 1
        
    def __iter__(self):
        """
        If we are asked to loop over the items in a grid
        (for instance, if we pass one Sudoku instance as the argument
        to the initialization of another one) we simply list the
        known cell contents of the grid.
        """
        return iter(self.contents)
    
    def mark_progress(self):
        """Set progress True and clear fields that depended on old state."""
        self.progress = True
        self.pairs = None
        
    def log(self,items,explanation=None):
        """
        Send a message for verbose output.
        Items should be a string or list of strings in the message.
        If explanation is not None, it is called as a function and
        the results appended to items.
        """
        if not self.logstream:
            return
        if isinstance(items,str):
            items = [items]
        if explanation:
            if isinstance(explanation,str) or isinstance(explanation,list):
                x = explanation
            else:
                x = explanation()
            if isinstance(x,str):
                x = [x]
        else:
            x = []
        text = ' '.join([str(i) for i in items+x])
        for line in wrap(text):
            self.logstream.write(line+'\n')
        self.logstream.write('\n')
        self.logstream.flush()

    def place(self,digit,cell,explanation=None):
        """Change the puzzle by filling the given cell with the given digit."""
        if digit != int(digit) or not 1 <= digit <= 9:
            raise ValueError("place(%d,%d): digit out of range" % (digit,cell))
        if self.contents[cell] == digit:
            return
        if self.contents[cell]:
            self.log(["Unable to place",digit,"in",cellnames[cell],
                      "as it already contains",str(self.contents[cell])+"."])
            raise BadSudoku("place(%d,%d): cell already contains %d" %
                            (digit,cell,self.contents[cell]))
        if (1<<cell) & self.locations[digit] == 0:
            self.log(["Unable to place",digit,"in",cellnames[cell],
                      "as that digit is not available to be placed there."])
            raise BadSudoku("place(%d,%d): location not available" %
                            (digit,cell))
        self.contents[cell] = digit
        bit = 1 << cell
        for d in digits:
            if d != digit:
                self.unplace(d,bit,explanation,False)
            else:
                self.unplace(d,neighbors[cell],explanation,False)
        self.mark_progress()
        self.log(["Placing",digit,"in",cellnames[cell]+'.'],explanation)

    def unplace(self,digit,mask,explanation=None,log=True):
        """
        Eliminate the masked positions as possible locations for digit.
        The log argument should be true for external callers, but false
        when called by Sudoku.place; it is used to disable verbose output
        that would be redundant to the output from place.
        """
        if digit != int(digit) or not 1 <= digit <= 9:
            raise ValueError("unplace(%d): digit out of range" % digit)
        if self.locations[digit] & mask:
            if log and self.logstream:
                items = ["Preventing",digit,"from being placed in",
                         namecells(self.locations[digit] & mask,"or")+'.']
                self.log(items,explanation)
            self.locations[digit] &=~ mask
            self.mark_progress()

    def choices(self,cell):
        """Which digits are still available to be placed in the cell?"""
        bit = 1<<cell
        return [d for d in digits if self.locations[d] & bit]

    def complete(self):
        """True if all cells have been filled in."""
        return 0 not in self.contents

# ======================================================================
#   Rules for puzzle solver
# ======================================================================

def locate(grid):
    """
    Place digits that can only go in one cell of their group.
    If a digit x has only one remaining cell that it can be placed in,
    within some row, column, or square, then we place it in that cell.
    Any potential positions of x incompatible with that cell (because
    they lie in the same row, column, or square) are removed from
    future consideration.
    """
    for d in digits:
        for g in groups:
            dglocs = grid.locations[d] & g.mask
            if dglocs & (dglocs-1) == 0:
                if dglocs == 0:
                    grid.log(["Unable to place",d,"anywhere in",g.name+"."])
                    raise BadSudoku("No place for %d in %s" %(d,g.name))
                grid.place(d,unmask[dglocs],
                            ["It is the only cell in",g.name,
                             "in which",d,"can be placed."])

def eliminate(grid):
    """
    Fill cells that can only contain one possible digit.
    If a cell has only one digit x that can be placed in it, we place
    x in that cell.  Incompatible positions for x are removed from
    future consideration.
    """
    for cell in range(81):
        if not grid.contents[cell]:
            allowed = grid.choices(cell)
            if len(allowed) == 0:
                grid.log(["Unable to place any digit in",cellnames[cell]+"."])
                raise BadSudoku("No digit for cell %d" % cell)
            if len(allowed) == 1:
                grid.place(allowed[0],cell,
                           "No other digit may be placed in that cell.")

def align(grid):
    """
    Eliminate positions that leave no choices for another group.
    If the cells of a square that can contain a digit x all lie
    in a single row or column, we eliminate positions for x that
    are outside the square but inside that row or column.  Similarly,
    if the cells that can contain x within a row or column all lie
    in a single square, we eliminate positions that are inside that
    square but outside the row or column.
    """
    for d in digits:
        for g in groups:
            a = grid.locations[d] & g.mask
            if a in alignments:
                s = [x for x in alignments[a] if x != g][0]
                def explain():
                    un = grid.locations[d] & s.mask &~ a
                    if un & (un - 1):
                        this = "These placements"
                    else:
                        this = "This placement"
                    return [this, "would conflict with", namecells(a)+",",
                            "which are the only cells in", g.name,
                            "that can contain that digit."]
                grid.unplace(d, s.mask &~ a, explain)

enough_room = "To leave enough room for those digits, no other " \
              "digits may be placed in those cells."

def explain_pair(grid,digs,locs):
    """Concoct explanation for application of pair rule."""
    d1,d2 = digs
    g1 = [g for g in groups if
          grid.locations[d1] & g.mask == grid.locations[d1] & locs]
    g2 = [g for g in groups if
          grid.locations[d2] & g.mask == grid.locations[d2] & locs]
    for g in g1:
        if g in g2:
            ing = ["In", g.name+",", "digits", d1, "and", d2]
            break
    else:
        # unlikely to get here due to align rule applying before pair
        ing = ["In",(g1 and g1[0].name or "no group")+",", "digit", str(d1)+",",
               "and in",(g2 and g2[0].name or "no group")+",", "digit", str(d2)]
    return ing+["may only be placed in",namecells(locs)+".", enough_room]

def pair(grid):
    """
    Eliminate positions that leave no choices for two other digits.
    If two digits x and y each share the same two cells as the only
    locations they may be placed within some row, column, or square,
    then all other digits must avoid those two cells.
    """
    grid.pairs = pairs = {}
    for d in digits:
        for g in groups:
            dglocs = grid.locations[d] & g.mask
            fewerbits = dglocs & (dglocs - 1)
            if fewerbits & (fewerbits - 1) == 0:
                if d not in pairs.setdefault(dglocs,[d]):
                    pairs[dglocs].append(d)
                    for e in digits:
                        if e not in pairs[dglocs]:
                            def explain():
                                return explain_pair(grid,pairs[dglocs],dglocs)
                            grid.unplace(e, dglocs, explain)

def triad(grid):
    """
    Find forced triples of digits within triples of cells.
    If some three cells, formed by intersecting a row or column
    with a square, have three digits whose only remaining positions
    within that row, column, or square are among those three cells,
    we prevent all other digits from being placed there.  We also
    remove positions for those three forced digits outside the
    triple but within the row, column, or square containing it.
    """
    for mask,sqr,grp in triads:
        forces = [d for d in digits
                  if (grid.locations[d]&sqr.mask == grid.locations[d]&mask)
                  or (grid.locations[d]&grp.mask == grid.locations[d]&mask)]
        if len(forces) == 3:
            outside = (sqr.mask | grp.mask) &~ mask
            for d in digits:
                def explain():
                    ing = ["In", grp.name, "and", sqr.name+",",
                           "digits %d, %d, and %d" % tuple(forces),
                           "may only be placed in", namecells(mask)+"."]
                    if d not in forces:
                        return ing+[enough_room]
                    elif grid.locations[d]&sqr.mask == grid.locations[d]&mask:
                        og = grp.name
                    else:
                        og = sqr.name
                    return ing+["Therefore,", d, "may not be placed",
                                "in any other cell of", og]

                grid.unplace(d, d in forces and outside or mask, explain)

def nishio(grid):
    """
    Remove incompatible positions of a single digit.
    If the placement of digit x in cell y can not be extended to a
    placement of nine copies of x covering each row, column, and
    square of the grid exactly once, we eliminate cell y from
    consideration as a placement for x.
    """

    def search(v):
        """Simple recursive DFS to compute a set of reachable vertices.
        Uses sets of visible and completable nodes in parent function,
        and returns the union of edge labels on placement graph paths."""
        visited.add(v)
        result = 0
        for w in FullPlacementGraph[v]:         # for each potential neighbor
            if locs & FullPlacementGraph[v][w]: # is it really a neighbor?
                if w not in visited:
                    result |= search(w)
                if w in completable:
                    completable.add(v)
                    result |= FullPlacementGraph[v][w]
        return result

    for d in digits:
        visited = {511}           # nodes no longer needing to be searched
        completable = {511}       # nodes with paths to the all-ones matrix
        locs = grid.locations[d]
        mask = search(0)          # bitmask of cells in valid placements
        if locs != mask:
            def explain():
                masked = locs &~ mask
                if masked &~ (masked - 1):
                    ex = "These cells are"
                else:
                    ex = "This cell is"
                return ex + " not part of any valid placement of this digit that covers each row, column and 3x3 square exactly once."

            grid.unplace(d, locs &~ mask, explain)

def rectangles():
    """Generate pairs of rows and columns that form two-square rectangles."""
    for r1 in rows:
        for r2 in rows:
            if r2 in nearby[r1]:
                for c1 in range(9):
                    for c2 in range(c1):
                        if cols[c1] not in nearby[cols[c2]]:
                            yield r1,r2,cols[c2],cols[c1]
            elif r1.mask < r2.mask:
                for c1 in cols:
                    for c2 in nearby[c1]:
                        yield r1,r2,c1,c2

def rectangle(grid):
    """
    Avoid the formation of an ambiguous rectangle.
    That is, four corners of a rectangle within two squares, all four
    corners initially blank, and containing only two digits. If this
    situation occurred, the puzzle would necessarily have evenly many
    solutions, because we could swap the two digits in the rectangle
    corners in any solution to form a different solution, contradicting
    the assumption that there is only one. Therefore, we make sure that
    any such rectangle keeps at least three available values.
    """
    if not grid.assume_unique:
        return
    for r1,r2,c1,c2 in rectangles():
        mask = (r1.mask | r2.mask) & (c1.mask | c2.mask)
        if not (mask & grid.original_cells):
            # First rectangle test
            # If three cells are bivalued with the same two digits x,y
            # then we can eliminate x and y on the fourth
            safe_corners = 0
            multiply_placable = []
            for d in digits:
                dmask = grid.locations[d] & mask
                if dmask & (dmask - 1):
                    multiply_placable.append(d)
                else:
                    safe_corners |= dmask
            if len(multiply_placable) == 2 and \
                    safe_corners & (safe_corners-1) == 0:
                for d in multiply_placable:
                    def explain():
                        return ["This placement would create an ambiguous",
                                "rectangle for digits",
                                str(multiply_placable[0]),"and",
                                str(multiply_placable[1]),"in",
                                r1.name+",",r2.name+",",
                                c1.name+",","and",c2.name+"."]
                    grid.unplace(d,safe_corners,explain)

            # Second rectangle test
            # If only three digits can be placed in the rectangle,
            # we eliminate placements that conflict with
            # all positions of one of the digits.
            placable = [d for d in digits if grid.locations[d] & mask]
            if len(placable) == 3:
                for d in placable:
                    a = grid.locations[d] & mask
                    conflicts = 0
                    for g in groups:
                        if grid.locations[d] & g.mask & a == a:
                            conflicts |= g.mask
                    def explain():
                        un = conflicts &~ a
                        if un & (un - 1):
                            this = "These placements"
                        else:
                            this = "This placement"
                        return ["The rectangle in", r1.name+",",
                                r2.name+",", c1.name+", and", c2.name,
                                "can only contain digits",
                                andlist([str(dd) for dd in placable])+".",
                                this, "would conflict with the placements",
                                "of", str(d)+",", "creating an ambiguous",
                                "rectangle on the remaining two digits."]
                    grid.unplace(d, conflicts &~ a, explain)

            # Third rectangle test
            # If two cells are bivalued with digits x and y,
            # and the other two cells are bilocal with x,
            # then we can eliminate y from the two bilocal cells.
            for x1,x2 in ((r1,r2), (r2,r1), (c1,c2), (c2,c1)):
                xd = [d for d in digits if grid.locations[d] & mask & x1.mask]
                if len(xd) == 2:    # found locked pair on x1's corners
                    for d in xd:
                        x2d = grid.locations[d] & x2.mask
                        if x2d & mask == x2d:   # and bilocal on x2
                            dd = xd[0]+xd[1]-d  # other digit
                            def explain():
                                return ["The rectangle in", r1.name+",",
                                    r2.name+",", c1.name+", and", c2.name,
                                    "can only contain digits",
                                    str(xd[0]),"and",str(xd[1]),"in",
                                    x1.name+".","In addition,"
                                    "the only cells in",x2.name,
                                    "that can contain",str(d),
                                    "are in the rectangle.",
                                    "Therefore, to avoid creating an",
                                    "ambiguous rectangle, the",str(dd),
                                    "in",x2.name,"must be placed",
                                    "outside the rectangle."]
                            grid.unplace(dd,x2d,explain)

            # Fourth rectangle test
            # If two cells are bivalued with digits x and y,
            # and a perpendicular side is bilocal with x,
            # then we can eliminate y from the remaining cell
            for x1,perp in ((r1,(c1,c2)),(r2,(c1,c2)),
                            (c1,(r1,r2)),(c2,(r1,r2))):
                xd = [d for d in digits if grid.locations[d] & mask & x1.mask]
                if len(xd) == 2:    # found locked pair on x1's corners
                    for x2 in perp:
                        for d in xd:
                            x2d = grid.locations[d] & x2.mask
                            if x2d & mask == x2d:   # and bilocal on x2
                                dd = xd[0]+xd[1]-d  # other digit
                                def explain():
                                    return ["For the rectangle in", r1.name+",",
                                        r2.name+",", c1.name+", and", c2.name,
                                        "the two corners in",
                                        x1.name,"must contain both digits",
                                        str(xd[0]),"and",str(xd[1]),
                                        "and the two corners in",
                                        x2.name,"must contain one",str(d)+".",
                                        "Therefore, to avoid creating an",
                                        "ambiguous rectangle, the",
                                        "remaining corner must not contain",
                                        str(dd)+"."]
                                grid.unplace(dd,mask&~(x1.mask|x2.mask),explain)

def trapezoid(grid):
    """
    Force pairs of digits to form trapezoids instead of rectangles.
    If two digits can only be placed in five cells of two squares,
    four of which form a rectangle, then they must be placed in
    four cells that form a trapezoid out of those five.
    We prevent those digits from being placed in cells not part of
    a trapezoid, and prevent other digits from being placed in cells
    that are part of all such trapezoids.
    """
    if not grid.assume_unique:
        return
    for r1,r2,c1,c2 in rectangles():
        corners = (r1.mask | r2.mask) & (c1.mask | c2.mask)
        if not (corners & grid.original_cells):
            s1,s2 = [s for s in sqrs if s.mask & corners]
            uncorner = (s1.mask | s2.mask) &~ corners
            candidates = {}
            universal = None
            for d in digits:
                if not grid.locations[d] & uncorner:
                    universal = d   # can form five cells w/any other digit
            for d in digits:
                locs_for_d = grid.locations[d] & uncorner
                if locs_for_d and not (locs_for_d & (locs_for_d - 1)):
                    if universal != None or locs_for_d in candidates:
                        # found another digit sharing same five cells w/d
                        if universal != None:
                            d1,d2 = universal,d
                        else:
                            d1,d2 = candidates[locs_for_d],d
                        explanation = ["Digits",str(d1),"and",str(d2),
                                       "must be placed in a trapezoid in",
                                       s1.name,"and",s2.name+",",
                                       "for if they were placed in a",
                                       "rectangle, their locations",
                                       "could be swapped, resulting",
                                       "in multiple solutions",
                                       "to the puzzle."]
                        must = locs_for_d
                        mustnt = 0
                        if s2.mask & locs_for_d:
                            s1,s2 = s2,s1   # swap so s1 contains extra cell
                        must |= corners & s2.mask
                        for line in r1.mask,r2.mask,c1.mask,c2.mask:
                            if line & locs_for_d and line & s2.mask:
                                # most informative case: the extra cell
                                # lies on a line through both squares.
                                must |= corners & (s1.mask &~ line)
                                mustnt |= corners & (s1.mask & line)
                        for d3 in digits:
                            if d3 == d1 or d3 == d2:
                                grid.unplace(d3,mustnt,explanation)
                            else:
                                grid.unplace(d3,must,explanation)
                    else:
                        candidates[locs_for_d] = d

def subproblem(grid):
    """
    Remove incompatible positions within a single row, column, or square.
    If the placement of a digit x in cell y within a single row, column,
    or square can not be extended to a complete solution of that row, column,
    or square, then we eliminate that placement from consideration.
    """
    for g in groups:
        graph = {}
        for d in digits:
            graph[d] = []
            locs = grid.locations[d] & g.mask
            while locs:
                bit = locs &~ (locs-1)
                graph[d].append(unmask[bit])
                locs &=~ bit
        imp = imperfections(graph)
        for d in list(imp.keys()):
            if not imp[d]:
                del imp[d]
        while imp:

            # Here with imp mapping digits to unplaceable cells.
            # We choose carefully the order of digits to handle,
            # so that our explanations make logical sense: if an
            # explanation includes the fact that a digit can only
            # go in certain cells, we need to have already handled
            # the unplaceable cells for that other digit.
            for d in imp:
                entailed = False
                for cell in imp[d]:
                    for forced in imp[d][cell]:
                        if forced in imp and imp[forced]:
                            entailed = True
                            break
                if not entailed:
                    break
                    
            # Here with imp[d] mapping d to some unplaceable cells.
            # We build up a bitmap of those cells, as we do collecting
            # the sets of digits and cells that must be matched to each
            # other and that prevent us from placing d in those cells.
            mask = 0
            forces = []
            for cell in imp[d]:
                bit = 1<<cell
                if bit & grid.locations[d]:
                    mask |= bit
                    force = imp[d][cell]
                    if force not in forces:
                        forces.append(force)
                        
            # Now that we have both the bitmap and the subgraphs describing
            # why each bit is in that bitmap, we are ready to make and
            # explain our unplacement decision.
            def explain():
                that = "would make it impossible to place that digit."
                expls = []
                for force in forces:
                    if expls or len(force) > 1:
                        that = "would leave too few remaining cells" \
                               " to place those digits."
                    if expls:
                        expls[-1] += ','
                        if force == forces[-1]:
                            expls[-1] += ' and'
                    forcedigs = [str(x) for x in force]
                    forcedigs.sort()
                    forcemask = 0
                    for dig in force:
                        for cell in force[dig]:
                            forcemask |= 1<<cell
                    expls += [len(forcedigs) == 1 and "digit" or "digits",
                              andlist(forcedigs), "can only be placed in",
                              namecells(forcemask)]
                expls[-1] += '.'
                return ["In", g.name+","] + expls + ["Placing", d,
                    "in", namecells(mask,"or"), that]
            grid.unplace(d,mask,explain)
            del imp[d]
        if grid.progress:
            return  # let changes propagate before trying more groups

bilocal_explanation = \
    "each two successive cells belong to a common row, column, or square," \
    " and are the only two cells in that row, column, or square where one" \
    " of the digits may be placed"
    
incyclic = "In the cyclic sequence of cells"
inpath = "In the sequence of cells"

def bilocal(grid):
    """
    Look for nonrepetitive cycles among bilocated digits.
    Despite the sesquipedalian summary line above, this is a form of
    analysis that is easy to perform by hand: draw a graph connecting
    two cells whenever some digit's location within a row, column,
    or square is forced to lie only in those two cells.  We then
    search for cycles in the graph in which each two adjacent edges
    in the cycle have different labels. In any such cycle, each cell
    can only contain the digits labeling the two edges incident to it.
    """
    if not grid.pairs:
        return  # can only run after pair rule finds edges

    # Make labeled graph of pairs
    graph = dict([(i,{}) for i in range(81)])
    for pair in grid.pairs:
        digs = grid.pairs[pair]
        bit = pair &~ (pair-1)
        pair &=~ bit
        if pair:
            v = unmask[bit]
            w = unmask[pair]
            graph[v][w] = graph[w][v] = digs
    
    # Apply repetitivity analysis to collect cyclic labels at each cell
    grid.bilocation = nrg = NonrepetitiveGraph(graph)
    forced = [set() for i in range(81)]
    for v,w,L in nrg.cyclic():
        forced[v].add(L)
        forced[w].add(L)

    # Carry out forces indicated by our analysis
    for cell in range(81):
        if len(forced[cell]) == 2:
            # It's also possible for len(forced[cell]) to be > 2;
            # in this case multiple cycles go through the same edge
            # and cell must be filled with the digit labeling that edge.
            # But for simplicity's sake we ignore that possibility;
            # it doesn't happen very often and when it does the repetitive
            # cycle rule will find it instead.
            mask = 1<<cell
            for d in digits:
                if d not in forced[cell]:
                    def explain():
                        forced1,forced2 = tuple(forced[cell])
                        cycle = nrg.shortest(cell,forced1,cell,forced2)
                        return [incyclic, pathname(cycle)+",",
                                bilocal_explanation + ".",
                                "This placement would prevent",
                                forced1, "or", forced2,
                                "from being placed in", cellnames[cell]+",",
                                "making it impossible to place the cycle's",
                                len(cycle)-1, "digits into the remaining",
                                len(cycle)-2, "cells."]
                    grid.unplace(d,mask,explain)

bivalue_explanation = \
    "each cell has two possible digits, each of which may also" \
    " be placed at one of the cell's two neighbors in the sequence"

def bivalue(grid):
    """
    Look for nonrepetitive cycles among bivalued cells.
    We draw a graph connecting two cells whenever both can only
    contain two digits, one of those digits is the same for both
    cells, and both cells belong to the same row, column, or square.
    Edges are labeled by the digit(s) the two cells share.
    If any edge of this graph is contained in a cycle with no two
    consecutive edges having equal labels, then the digit labeling
    that edge must be placed on one of its two endpoints, and can
    not be placed in any other cell of the row, column, or square
    containing the edge.
    """
    
    # Find and make bitmask per digit of bivalued cells
    graph = {}
    grid.otherbv = otherbv = {}
    tvmask = [0]*10
    for c in range(81):
        ch = grid.choices(c)
        if len(ch) == 2:
            graph[c] = {}
            tvmask[ch[0]] |= 1<<c
            tvmask[ch[1]] |= 1<<c
            otherbv[c,ch[0]] = ch[1]
            otherbv[c,ch[1]] = ch[0]
    edgegroup = {}
    
    # Form edges and map back to their groups
    for g in groups:
        for d in digits:
            mask = tvmask[d] & g.mask
            dgcells = []
            while mask:
                bit = mask &~ (mask - 1)
                dgcells.append(unmask[bit])
                mask &=~ bit
            for v in dgcells:
                for w in dgcells:
                    if v != w:
                        edgegroup.setdefault((v,w),[]).append(g)
                        graph[v].setdefault(w,set()).add(d)

    # Apply repetitivity analysis to collect cyclic labels at each cell
    # and eliminate that label from other cells of the same group
    grid.bivalues = nrg = NonrepetitiveGraph(graph)
    for v,w,digit in nrg.cyclic():
        mask = 0
        for g in edgegroup[v,w]:
            mask |= g.mask
        mask &=~ (1 << v)
        mask &=~ (1 << w)
        def explain():
            cycle = [v] + nrg.shortest(w,grid.otherbv[w,digit],
                                       v,grid.otherbv[v,digit])
            return ["In the cyclic sequence of cells", pathname(cycle)+",",
                    bivalue_explanation + ".",
                    "This placement would conflict with placing", digit,
                    "in", namecells((1<<v)|(1<<w))+",",
                    "making it impossible to fill the cycle's",
                    len(cycle)-1, "cells with the remaining",
                    len(cycle)-2, "digits."]
        grid.unplace(digit,mask,explain)

def repeat(grid):
    """
    Look for cycles of bilocated or bivalued vertices with one repetition.
    We use the same graphs described for the bilocal and bivalue rules;
    if there exists a cycle in which some two adjacent edges are labeled
    by the same digit, and all other adjacent pairs of cycle edges have
    differing digits, then the repeated digit must be placed at the cell
    where the two same-labeled edges meet (in the case of the bilocal graph)
    or can be eliminated from that cell (in the case of the bivalue graph).
    """
    if not grid.bilocation or not grid.bivalues:
        return
    for cell in range(81):
        if not grid.contents[cell]:
            for d in grid.choices(cell):
                if (cell,d) in grid.bilocation.reachable(cell,d):
                    cycle = grid.bilocation.shortest(cell,d,cell,d)
                    if cycle[1] == cycle[-2]:
                        # Degenerate repetitive cycle, look for a better one.
                        # It would be a correct decision to place d in cell:
                        # due to prior application of the bilocal rule, the
                        # part of the cycle from cycle[1] to cycle[-2] must
                        # itself be a repetitive cycle. But the explanation
                        # will be clearer if we avoid using this cycle.
                        break
                    def explain():
                        expl = [incyclic, pathname(cycle)+",",
                                bilocal_explanation + ".",
                                "If",d,"were not placed in",cellnames[cell]+",",
                                "it would have to be placed in",
                                cellnames[cycle[1]],"and",
                                cellnames[cycle[-2]],"instead,",
                                "making it impossible to place the"]
                        if len(cycle) == 4:
                            expl.append("remaining digit.")
                        else:
                            expl += ["cycle's remaining",len(cycle)-3,"digits",
                                     "in the remaining"]
                            if len(cycle) == 5:
                                expl.append("cell.")
                            else:
                                expl += [len(cycle)-4,"cells."]
                        return expl
                    grid.place(d,cell,explain)
                    return  # allow changes to propagate w/simpler rules
                elif (cell,d) in grid.bivalues.reachable(cell,d):
                    cycle = grid.bivalues.shortest(cell,d,cell,d)
                    if cycle[1] == cycle[-2]:
                        break
                    def explain():
                        return [incyclic, pathname(cycle)+",",
                                bivalue_explanation + ",",
                                "except that", cellnames[cell],
                                "shares", d, "as a possible value",
                                "with both of its neighbors.",
                                "Placing", d, "in", cellnames[cell],
                                "would make it impossible",
                                "to fill the cycle's remaining",
                                len(cycle)-2, "cells with the remaining",
                                len(cycle)-3, "digits, so only",
                                grid.otherbv[cell,d], "can be placed in",
                                cellnames[cell]+"."]
                    grid.place(grid.otherbv[cell,d],cell,explain)
                    return  # allow changes to propagate w/simpler rules

def path(grid):
    """
    Look for paths of bilocated or bivalued cells with conflicting endpoints.
    In the same graphs used by the bilocal and repeat rules, if there exists
    a path that starts and ends with the same digit, with no two consecutive
    edges labeled by the same digit, then the digit ending the path can be
    placed in no cell that conflicts with both endpoints of the path.  If
    the path endpoints belong to the same row, column, or square as each other,
    this eliminates other placements within that row, column, or square;
    otherwise, it eliminates placements at the other two corners of a
    rectangle having the two path endpoints as opposite corners.
    """
    if not grid.bilocation or not grid.bivalues:
        return
    for cell in range(81):
        if not grid.contents[cell]:
            for d in grid.choices(cell):
                for neighbor,nd in grid.bilocation.reachable(cell,d):
                    if nd == d:
                        def explain():
                            path = grid.bilocation.shortest(cell,d,neighbor,d)
                            return [inpath, pathname(path)+",",
                                    bilocal_explanation+".",
                                    "This placement conflicts with placing",
                                    d, "in", cellnames[cell], "or",
                                    cellnames[neighbor]+",", "making it",
                                    "impossible to place the sequence's",
                                    len(path)-1, "digits in the remaining",
                                    len(path)-2, "cells."]
                        grid.unplace(d,neighbors[cell]&neighbors[neighbor],
                                     explain)
                if cell in grid.bivalues:
                    for neighbor,nd in grid.bivalues.reachable(cell,
                                                grid.otherbv[cell,d]):
                        if d == grid.otherbv[neighbor,nd]:
                            def explain():
                                path = grid.bivalues.shortest(cell,
                                        grid.otherbv[cell,d],neighbor,nd)
                                return [inpath, pathname(path)+",",
                                        bivalue_explanation+".",
                                        "This placement conflicts with placing",
                                        d, "in", cellnames[cell], "or",
                                        cellnames[neighbor]+",", "making it",
                                        "impossible to fill the sequence's",
                                        len(path), "cells using only the",
                                        len(path)-1,
                                        "shared digits of the sequence."]
                            grid.unplace(d,neighbors[cell]&neighbors[neighbor],
                                         explain)

def explain_conflict_path(grid,cell,d,why,reached,dd):
    """Explain why either cell,d or reached,dd must be placed."""
    if why[reached,dd]:
        path = grid.bilocation.shortest(cell,d,reached,dd)
        if len(path) == 2:
            mask = (1<<cell)|(1<<reached)
            for g in groups:
                if g.mask & mask == mask:
                    break
            return [cellnames[cell],"and",cellnames[reached],
                    "are the only cells in",g.name,
                    "in which",d,"may be placed, so if",d,
                    "were not placed in",cellnames[cell]+",",
                    "it would have to be placed in",cellnames[reached]+"."]
        return [inpath, pathname(path)+",", bilocal_explanation+".",
                "If",d,"were not placed in",cellnames[cell]+",",
                "then",dd,"would have to be placed in",cellnames[reached]+",",
                "in order to make room for the remaining",
                plural(len(path)-2,"digit"),"in the remaining",
                plural(len(path)-2,"cell"),"of the sequence."]
    path = grid.bivalues.shortest(cell,grid.otherbv[cell,d],
                                 reached,grid.otherbv[reached,dd])
    if len(path) == 2:
        mask = (1<<cell)|(1<<reached)
        return [cellnames[cell],"and",cellnames[reached],
                "each have two possible values.",
                "If",d,"were not placed in",cellnames[cell],
                "it would have to contain",grid.otherbv[cell,d],
                "instead, forcing",cellnames[reached],"to contain",str(dd)+"."]
    return [inpath, pathname(path)+",", bivalue_explanation+".",
            "If",d,"were not placed in",cellnames[cell]+",",
            "then",dd,"would have to be placed in",cellnames[reached]+",",
            "in order to make allow the remaining",plural(len(path)-1,"cell"),
            "of the sequence to be filled by the remaining",
            plural(len(path)-1,"digit")+"."]
    

def explain_conflict(grid,cell,d,why,reached,dd):
    """Concoct explanation for pair of conflicting paths, one to reached."""
    for neighbor,ddd in why:
        if ddd == dd:
            if (1<<neighbor) & neighbors[reached]:
                return explain_conflict_path(grid,cell,d,why,reached,dd) + \
                       explain_conflict_path(grid,cell,d,why,neighbor,dd) + \
                       [cellnames[reached],"and",cellnames[neighbor],
                        "cannot both contain",str(dd)+",","so",cellnames[cell],
                        "must contain",str(d)+"."]
    return explain_conflict_path(grid,cell,d,why,reached,dd) + \
        ["This conflicts with another path that has become lost."]

def explain_conflict_group(grid,cell,d,why,g,dd):
    """Conflict explanation for set of conflicting paths that cover a group."""
    mask = g.mask & grid.locations[dd]
    conflicts = []
    confmask = 0
    for reached,ddd in why:
        if dd == ddd and neighbors[reached] & mask:
            conflicts.append(reached)
            confmask |= 1<<reached
            mask &=~ neighbors[reached]
    conflicts.sort()
    expl = []
    for c in conflicts:
        expl += explain_conflict_path(grid,cell,d,why,c,dd)
    expl += ["In",g.name+",",namecells(g.mask&grid.locations[dd]),
             "are the only cells in which",dd,"may be placed."]
    return expl + ["Placing",dd,"in",namecells(confmask),
                   "would prevent it from being placed anywhere in",g.name+",",
                   "so",d,"must be placed in",cellnames[cell]+"."]

def conflict(grid):
    """
    Look for conflicting paths of bilocated or bivalued cells.
    In the same graph used by the bilocal and repeat rules, if there exist
    two paths that start with the same cell and digit, and that end with
    equal digits in different cells of the same row, column, or square,
    then the start cell must contain the starting digit for otherwise
    it would cause the end cells to conflict with each other.
    One or both paths can instead be in the bivalue graph, starting and
    ending with the other digit than the one for the bilocal path.
    We also find similar pairs of paths that end in sets of cells that
    together eliminate all positions for the end digit in another row,
    column, or square of the grid.
    """
    if not grid.bilocation or not grid.bivalues:
        return
    for cell in range(81):
        if not grid.contents[cell]:
            for d in grid.choices(cell):
                conflicts = [0]*10
                why = {}
                for reached,dd in grid.bilocation.reachable(cell,d):
                    why[reached,dd] = True
                    if (1<<reached) & conflicts[dd]:
                        def explain():
                            return explain_conflict(grid,cell,d,why,reached,dd)
                        grid.place(d,cell,explain)
                        return  # allow changes to propagate
                    else:
                        conflicts[dd] |= neighbors[reached]
                if cell in grid.bivalues:
                    for reached,dd in grid.bivalues.reachable(cell,
                                                grid.otherbv[cell,d]):
                        other = grid.otherbv[reached,dd]
                        why[reached,other] = False
                        if (1<<reached) & conflicts[other]:
                            def explain():
                                return explain_conflict(grid,cell,d,
                                                        why,reached,other)
                            grid.place(d,cell,explain)
                            return  # allow changes to propagate
                        else:
                            conflicts[other] |= neighbors[reached]
                for g in groups:
                    for dd in digits:
                        if grid.locations[dd] & g.mask &~ conflicts[dd] == 0:
                            def explain():
                                return explain_conflict_group(grid,cell,d,
                                                              why,g,dd)
                            grid.place(d,cell,explain)
                            return  # allow changes to propagate

def createimplication(mask,pos,digit,T):
    """Add to 2SAT instance a constraint that the given digit in any mask position forces the same digit at pos."""
    while mask:
        bit = mask &~ (mask - 1)
        mask &=~ bit
        T[unmask[bit],digit].append((pos,digit))

def pseudonishio(g1,g2,grid,T):
    """Create 2SAT constraints for block-block interactions involving a single digit. If placing the digit in some cell of one block eliminates all but one of the potential locations for the same digit in another block, create an implication between the initial cell and the remaining location."""
    if g1.mask & g2.mask == 0:
        return
    for d in digits:
        dg1 = grid.locations[d] & g1.mask
        dg2 = grid.locations[d] & g2.mask
        diff1 = dg1 &~ dg2
        diff2 = dg2 &~ dg1
        conj = dg1 & dg2
        if diff1 and diff2 and conj:
            if diff1 & (diff1 - 1) == 0:    # single bit in diff1
                createimplication(diff2,unmask[diff1],d,T)
            if diff2 & (diff2 - 1) == 0:    # single bit in diff2
                createimplication(diff1,unmask[diff2],d,T)

def twosat(grid):
    """Apply a general-purpose two-satisfiability solver."""

    # Check whether this sort of rule is allowed
    if not grid.twosat:
        return

    def twosat_explain():
        return "From conversion of the puzzle to a 2-satisfiability instance."
    T = {}
    
    # If a cell has value d, it can't also have value e
    for cell in range(81):
        if len(grid.choices(cell)) > 1:
            for d in grid.choices(cell):
                T[(cell,d)] = [Not((cell,e))
                                for e in grid.choices(cell)
                                if d != e]
                T[Not((cell,d))] = []
    
    # If a cell has value d, its neighbors can't have the same value
    for cell in range(81):
        if len(grid.choices(cell)) > 1:
            for neighbor in range(81):
                if cell != neighbor and (1<<neighbor) & neighbors[cell]:
                    for d in grid.choices(cell):
                        if d in grid.choices(neighbor):
                            T[(cell,d)].append(Not((neighbor,d)))

    # If a cell has only two possible values, one of them must be chosen
    # (one-step lookahead of eliminate rule)
    for cell in range(81):
        if len(grid.choices(cell)) == 2:
            x,y = grid.choices(cell)
            T[Not((cell,x))].append((cell,y))

            # Detect situations where one cell has two choices, and a neighbor
            # has a superset of three choices. The third choice of the neighbor
            # determines whether these two cells form a locked pair.
            # (one-step lookahead of pair rule)
            bothxy = grid.locations[x] & grid.locations[y] &~ (1<<cell)
            for g in groups:
                if g.mask & (1<<cell):
                    candidates = g.mask & bothxy
                    while candidates:
                        cellmask = candidates &~ (candidates - 1)
                        candidates &=~ cellmask
                        candidate = unmask[cellmask]
                        ch = grid.choices(candidate)
                        if len(ch) == 3:
                            thirdchoice = [z for z in ch if z not in [x,y]][0]
                            for dd in [x,y]:
                                other = grid.locations[dd] & g.mask &~ (1<<cell) &~ (1<<candidate)
                                while other:
                                    cellmask = other &~ (other - 1)
                                    other &=~ cellmask
                                    interference = unmask[cellmask]
                                    T[Not((candidate,thirdchoice))].append(
                                        Not((interference,dd)))

    # If a group has only two locations for a digit, one of them must be chosen
    # (one-step lookahead of locate rule)
    for d in digits:
        for g in groups:
            dglocs = grid.locations[d] & g.mask
            x = dglocs &~ (dglocs - 1)
            dglocs &=~ x
            y = dglocs &~ (dglocs - 1)
            dglocs &=~ y
            if x and y and not dglocs:
                x = unmask[x]
                y = unmask[y]
                T[Not((x,d))].append((y,d))
                
    # Detect situations when a digit in one block knocks out all but one
    # of the positions for that digit in another block
    # (one-step lookahead of align rule)
    for s in sqrs:
        for l in rows+cols:
            pseudonishio(s,l,grid,T)

    # Solve the system and interpret the results
    F = Forced(T)
    if F != None:
        for cell,digit in F:    # Do place first for fewer explanations
            if F[cell,digit]:
                grid.place(digit,cell,twosat_explain)
        for cell,digit in F:    # Now the unplaces
            if not F[cell,digit]:
                grid.unplace(digit,1<<cell,twosat_explain)

# triples of name, rule, difficulty level
rules = [
    ("locate",locate,0),
    ("eliminate",eliminate,0),
    ("align",align,1),
    ("pair",pair,1),
    ("triad",triad,1),
    ("trapezoid",trapezoid,1),
    ("rectangle",rectangle,1),
    ("subproblem",subproblem,2),
    ("nishio",nishio,2),
    ("bilocal",bilocal,3),
    ("bivalue",bivalue,3),
    ("repeat",repeat,3),
    ("path",path,3),
    ("conflict",conflict,4),
    ("twosat",twosat,5)
]

def step(grid, quick_and_dirty = False):
    """Try the rules, return True if one succeeds."""
    if grid.complete():
        return False
    grid.progress = False
    grid.steps += 1
    grid.log(["Beginning solver iteration",str(grid.steps)+'.'])
    for name,rule,level in rules:
        if level <= 1 or not quick_and_dirty:
            rule(grid)
            if grid.progress:
                grid.rules_used.add(name)
                grid.log(["Ending solver iteration",grid.steps,
                          "after successful application of the",
                          name,"rule."])
                return True
    grid.log(["Ending solver iteration",grid.steps,
              "with no additional progress."])
    return False

# ======================================================================
#   Random permutation of puzzles
# ======================================================================

def block_permutation(preserve_symmetry = True):
    """Choose order to rearrange rows or columns of blocks."""
    if preserve_symmetry:
        return random.choice([[0,1,2],[2,1,0]])
    result = [0,1,2]
    random.shuffle(result)
    return result

def permute1d(preserve_symmetry = True):
    """Choose order to rearrange rows or columns of puzzle."""
    bp = block_permutation(preserve_symmetry)
    ip = [block_permutation(False),block_permutation(preserve_symmetry)]
    if preserve_symmetry:
        ip.append([2-ip[0][2],2-ip[0][1],2-ip[0][0]])
    else:
        ip.append(block_permutation(False))
    return [bp[i]*3+ip[i][j] for i in [0,1,2] for j in [0,1,2]]

def permute(grid, preserve_symmetry = True):
    """Generate a randomly permuted version of the input puzzle."""
    digit_permutation = list(digits)
    random.shuffle(digit_permutation)
    digit_permutation = [0]+digit_permutation
    row_permutation = permute1d(preserve_symmetry)
    col_permutation = permute1d(preserve_symmetry)
    transpose = random.choice([[1,9],[9,1]])
    contents = [None]*81
    for row in range(9):
        for col in range(9):
            contents[row_permutation[row]*transpose[0] +
                     col_permutation[col]*transpose[1]] = \
                digit_permutation[grid.contents[9*row+col]]
    return Sudoku(contents)

# ======================================================================
#   Output of puzzles
# ======================================================================

# Output functions should return True if it's ok to add difficulty/level,
# false otherwise

def text_format(grid):
    output = []
    for row in digits:
        if row % 3 != 1:
            output.append(('|' + ' '*11)*3 + '|\n')
        elif row == 1:
            output.append(' ' + '-'*35 + ' \n')
        else:
            output.append('|' + '-'*35 + '|\n')
        for col in digits:
            if col % 3 == 1:
                output.append('| ')
            else:
                output.append('  ')
            digit = grid.contents[(row-1)*9+(col-1)]
            if digit:
                output += [str(digit), ' ']
            else:
                output.append('. ')
        output.append('|\n')
    output.append(' ' + '-'*35 + ' \n')
    print(''.join(output))
    return True

def numeric_format(grid):
    row = []
    for digit in grid:
        row.append(str(digit))
        if len(row) == 9:
            print(''.join(row))
            row = []
    return True

def html_format(grid):
    print("<table border=1>")
    for a in range(3):
        print("<tr>")
        for b in range(3):
            print("<td><table border=0>")
            for c in range(3):
                print("<tr>")
                for d in range(3):
                    row = 3*a+c
                    col = 3*b+d
                    cell = 9*row+col
                    if grid.contents[cell]:
                        print('<td width=30 height=30 align=center valign=middle style="font-family:times,serif; font-size:16pt; text-align:center; color:black">%d</td>' % grid.contents[cell])
                    else:
                        print('<td width=30 height=30 align=center valign=middle><input style="font-family:times,serif; font-size:16pt; text-align:center; color:#555; margin:0pt; border-width:0" size=1 maxlength=1></td>')
                print("</tr>")
            print("</table></td>")
        print("</tr>")
    print("</table>")
    return False

def svg_format(grid):
    svg = SVG(274+274j,sys.stdout)
    svg.group(style={"fill":"none", "stroke":"black", "stroke-width":"1.5"})
    svg.rectangle(2+2j,272+272j)
    for i in [3,6]:
        pos = 30*i+2
        svg.segment(2+pos*1j,272+pos*1j)
        svg.segment(pos+2j,pos+272j)
    svg.ungroup()
    svg.group(style={"fill":"none", "stroke":"black", "stroke-width":"0.5"})
    for i in [1,2,4,5,7,8]:
        pos = 30*i+2
        svg.segment(2+pos*1j,272+pos*1j)
        svg.segment(pos+2j,pos+272j)
    svg.ungroup()
    svg.group(style={"font-family":"Times", "font-size":"24", "fill":"black",
                     "text-anchor":"middle"})
    for row in range(9):
        for col in range(9):
            cell = row*9+col
            if grid.contents[cell]:
                svg.text(str(grid.contents[cell]),30*col+17+30j*row+25j)
    svg.ungroup()
    svg.close()
    return False

output_formats = {
    "text": text_format,
    "txt": text_format,
    "t": text_format,
    "numeric": numeric_format,
    "num": numeric_format,
    "n": numeric_format,
    "html": html_format,
    "h": html_format,
    "svg": svg_format,
    "s": svg_format,
}
    
# ======================================================================
#   Backtracking search for all solutions
# ======================================================================

def all_solutions(grid, fastrules = True):
    """Generate sequence of completed Sudoku grids from initial puzzle."""
    while True:
        # first try the usual non-backtracking rules
        try:
            while step(grid,fastrules): pass
        except BadSudoku:
            grid.log("A contradiction was found,"
                     " so this branch has no solutions.")
            return  # no solutions
    
        # if they finished off the puzzle, there's only one solution
        if grid.complete():
            grid.log("A solution to the puzzle has been found.")
            yield grid
            return
        
        # find a cell with few remaining possibilities
        def choices(c):
            ch = grid.choices(c)
            if len(ch) < 2: return (10,0,0)
            return (len(ch),c,ch[0])
        L,c,d = min([choices(c) for c in range(81)])
        
        # try it both ways
        branch = Sudoku(grid)
        grid.log("Failed to progress, "
                 "creating a new backtracking search branch.")
        branch.logstream = grid.logstream
        branch.steps = grid.steps
        branch.original_cells = grid.original_cells
        branch.place(d,c,"The backtracking search will try this placement"
                         " first. Then, after returning from this branch,"
                         " it will try preventing this placement.")
        for sol in all_solutions(branch,fastrules):
            yield sol
        grid.log(["Returned from backtracking branch; undoing placement of",
                  d,"in",cellnames[c],"and all subsequent decisions."])
        grid.rules_used.update(branch.rules_used)
        grid.rules_used.add("backtrack")
        grid.steps = branch.steps
        grid.unplace(d,1<<c,"The backtracking search has already tried this"
                     " placement, and now must try the opposite decision.")

def unisolvent(grid):
    """Does this puzzle have a unique solution?"""
    stream = all_solutions(grid)
    try:
        next(stream)
    except StopIteration:
        return False
    try:
        next(stream)
    except StopIteration:
        return True
    return False

# ======================================================================
#   Command-line interface
# ======================================================================

parser = OptionParser()

parser.add_option("-r","--rules",dest="show_rules", action="store_true",
                  help = "show description of known solver rules and exit")

parser.add_option("-l","--levels",dest="show_levels", action="store_true",
                  help = "show description of difficulty levels and exit")

parser.add_option("-0", "--blank", dest="empty", action="store_true",
                  help = "output blank sudoku grid and exit")

parser.add_option("-t","--translate", dest="translate", action="store_true",
                  help = "translate format of input puzzle without solving")

parser.add_option("-p","--permute",dest="permute", action="store_true",
                  help = "randomly rearrange the input puzzle")

parser.add_option("-g","--generate", dest="generate", action="store_true",
                  help = "generate new puzzle rather than reading from stdin")

parser.add_option("-a", "--asymmetric", dest="asymmetric", action="store_true",
                  help = "allow asymmetry in generated puzzles")

parser.add_option("-u", "--unique", dest="assume_unique", action="store_false",
                  help = "disallow rules that assume a unique solution",
                  default = True)

parser.add_option("-s", "--satisfiability", dest="twosat", action="store_true",
                  help = "enable 2-satisfiability solver")

parser.add_option("-b", "--backtrack", dest="backtrack", action="store_true",
                  help = "enable trial and error search for all solutions")

parser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                  help = "output description of each step in puzzle solution")

parser.add_option("-x", "--empty", dest="emptychars", action="store",
                  type="string", default=".0",
                  help="characters representing empty cells in input puzzle")

parser.add_option("-2", "--output-both", dest="output_both",
                  action="store_true",
                  help = "output both the puzzle and its solution")

parser.add_option("-f", "--format", dest="format", action="store",
                  type="string", default="text",
                  help="output format (options: text, numeric, html, svg)")

if __name__ == '__main__':
    options,args = parser.parse_args()
    if args:
        print("Unrecognized command line syntax, use --help for input documentation")
        sys.exit(0)
    
    if options.show_rules:
        print("""This solver knows the following rules.  Rules occurring later
in the list are attempted only when all earlier rules have failed
to make progress.
""")
        for name,rule,difficulty in rules:
            print(name + ":" + rule.__doc__)
        sys.exit(0)

    if options.show_levels:
        print("""
Puzzles are classified by difficulty, according to a weighted combination
of the set of rules needed to solve each puzzle.  There are six levels,
in order by difficulty: easy, moderate, tricky, difficult, evil, and
fiendish.  In addition, a puzzle is classified as impossible if this
program cannot find a solution for it, or if backtracking is needed to
find the solution.
""")
        sys.exit(0)

    if options.translate:
        if options.generate:
            print("Cannot simultaneously generate and translate puzzles.")
            sys.exit(0)
    
    try:
        outputter = output_formats[options.format.lower()]
    except KeyError:
        print("Unrecognized output format.")
        sys.exit(0)

    if options.empty:
        outputter(Sudoku())
        sys.exit(0)

# ======================================================================
#   Initial puzzle setup
# ======================================================================

def random_puzzle(generate_symmetric = True):
    """Generate and return a randomly constructed Sudoku puzzle instance."""
    puzzle = []
    grid = Sudoku()

    def choices(cell):
        c = grid.choices(cell)
        return len(c) > 1 and c or []

    while True:
        try:
            while not grid.complete():
                d,c = random.choice([(d,c) for c in range(81)
                                           for d in choices(c)])
                grid.place(d,c)
                while step(grid,True): pass
                puzzle.append((d,c))
                if generate_symmetric:
                    c = 80-c
                    ch = grid.choices(c)
                    if not ch:  # avoid IndexError from random.choice
                        raise BadSudoku("Placement invalidated symmetric cell")
                    d = random.choice(ch)
                    grid.place(d,c)
                    while step(grid,True): pass
                    puzzle.append((d,c))
        except BadSudoku:
            puzzle = []
            grid = Sudoku()
            continue
        break
    
    # find redundant information in initial state
    q = 0
    while q < len(puzzle):
        grid = Sudoku(puzzle[:q] + puzzle[q+1+generate_symmetric:])
        if not unisolvent(grid):
            q += 1+generate_symmetric
        else:
            del puzzle[q]
            if generate_symmetric:
                del puzzle[q]

    return Sudoku(puzzle)

def read_puzzle(empty = ".0"):
    """Read and return a Sudoku instance from standard input."""
    def digits():
        for digit in sys.stdin.read():
            if digit in empty:
                yield 0
            elif '1' <= digit <= '9':
                yield int(digit)
    return Sudoku(digits())

if __name__ == '__main__':
    if options.generate:
        puzzle = random_puzzle(not options.asymmetric)
        print_puzzle = True
        print_solution = options.output_both
    else:
        puzzle = read_puzzle(options.emptychars)
        print_puzzle = options.output_both or options.translate
        print_solution = options.output_both or not options.translate
    if options.permute:
        puzzle = permute(puzzle, not options.asymmetric)
    if options.verbose:
        puzzle.logstream = sys.stderr
    if options.assume_unique:
        puzzle.assume_unique = True
    if options.twosat:
        puzzle.twosat = True

# ======================================================================
#   Main program: print and solve puzzle
# ======================================================================

if __name__ == '__main__':
    print_level = True
    if print_puzzle:
        print_level = outputter(puzzle)
        
    if options.output_both and print_level:
        print
    
    if options.backtrack:
        solns = all_solutions(puzzle,False)
    else:
        while step(puzzle): pass
        solns = [puzzle]

    nsolns = 0
    for soln in solns:    
        if print_solution:
            print_level = outputter(soln)
        nsolns += 1

    difficulty = 0
    used_names = []
    for name,rule,level in rules:
        if name in puzzle.rules_used:
            used_names.append(name)
            difficulty += (1<<level) - 1
    if "backtrack" in puzzle.rules_used:
        used_names.append("backtrack")
    if print_level:
        print("\nRules used:" + (", ".join(used_names)))
        if nsolns != 1:
            print("Number of solutions: %d" % nsolns)
        if not puzzle.complete() or "backtrack" in puzzle.rules_used:
            print("Level: impossible")
        elif difficulty <= 0:
            print("Level: easy")
        elif difficulty <= 5:
            print("Level: moderate")
        elif difficulty <= 9:
            print("Level: tricky")
        elif difficulty <= 17:
            print("Level: difficult")
        elif difficulty <= 33:
            print("Level: evil")
        else:
            print("Level: fiendish")
