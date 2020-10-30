"""CubicHam.py

Generate all Hamiltonian cycles in graphs of maximum degree three.
D. Eppstein, April 2004.
"""

import unittest
from Graphs import *
from Biconnectivity import isBiconnected
from CardinalityMatching import matching
from Util import arbitrary_item, map_to_constant

def HamiltonianCycles(G):
    """
    Generate a sequence of all Hamiltonian cycles in graph G.
    G should be represented in such a way that "for v in G" loops through
    the vertices, and "G[v]" produces a collection of neighbors of v; for
    instance, G may be a dictionary mapping vertices to lists of neighbors.
    Each cycle is returned as a graph in a similar representation, and
    should not be modified by the caller.  Running time is O(2^{3n/8}) as
    analyzed in my paper, The Traveling Salesman Problem for Cubic Graphs.
    """

    # Check input and copy it so we can modify the copy.
    # In the copied graph G, G[v][w] is True when vw is an original edge
    # of the input, and False when it was produced by a contraction.
    if not G or not isUndirected(G) or maxDegree(G) > 3:
        raise ValueError("HamiltonianCycles input must be undirected degree three graph")
    if minDegree(G) < 2:
        return
    G = copyGraph(G,map_to_constant(True))

    # Subgraph of forced edges in the input
    forced_in_input = {v:{} for v in G}

    # Subgraph of forced edges in current G
    forced_in_current = {v:{} for v in G}

    # List of vertices with degree two
    degree_two = [v for v in G if len(G[v]) == 2]

    # Collection of vertices with forced edges
    forced_vertices = {}

    # Reuse results of call to matching() to speed up subsequent calls
    previous_matching = {}

    # The overall backtracking algorithm is implemented by means of
    # a stack of actions.  At each step we pop the most recent action
    # off the stack and call it.  Each stacked function should return None or False
    # normally, or True to signal that we have found a Hamiltonian cycle.
    # Whenever we modify the graph, we push an action undoing that modification.
    # Below are definitions of actions and action-related functions.

    def remove(v,w):
        """Remove edge v,w from edges of G."""
        was_original = G[v][w]
        del G[v][w],G[w][v]
        was_forced = w in forced_in_current[v]
        if was_forced:
            del forced_in_current[v][w],forced_in_current[w][v]

        def unremove():
            G[v][w] = G[w][v] = was_original
            if was_forced:
                forced_in_current[v][w] = forced_in_current[w][v] = True

        actions.append(unremove)

    def now_degree_two(v):
        """Discover that changing G has caused v's degree to become two."""
        degree_two.append(v)
        def not_degree_two():
            top = degree_two.pop()
            assert v == top
        actions.append(not_degree_two)

    def safely_remove(v,w):
        """
        Remove edge v,w and update degree two data structures.
        Returns True if successful, False if found a contradiction.
        """
        assert w in G[v]
        if w in forced_in_current[v] or len(G[v]) < 3 or len(G[w]) < 3:
            return False
        remove(v,w)
        now_degree_two(v)
        now_degree_two(w)
        return True

    def remove_third_leg(v):
        """
        Check if v has two forced edges and if so remove unforced one.
        Returns True if successful, False if found a contradiction.
        """
        if len(G[v]) != 3 or len(forced_in_current[v]) != 2:
            return True
        w = [x for x in G[v] if x not in forced_in_current[v]][0]
        if len(G[w]) <= 2:
            return False
        return safely_remove(v,w)

    def force(v,w):
        """
        Add edge v,w to forced edges.
        Returns True if successful, False if found a contradiction.
        """
        if w in forced_in_current[v]:
            return True     # Already forced, nothing to do
        if len(forced_in_current[v]) > 2 or len(forced_in_current[w]) > 2:
            return False    # Three incident forced => no cycle exists
        if w not in G[v] or v not in G[w]:
            return False    # Removed from G after we decided to force it?
        forced_in_current[v][w] = forced_in_current[w][v] = True
        not_previously_forced = [x for x in (v,w) if x not in forced_vertices]
        for x in not_previously_forced:
            forced_vertices[x] = True
        was_original = G[v][w]
        if was_original:
            forced_in_input[v][w] = forced_in_input[w][v] = True

        def unforce():
            """Undo call to force."""
            for x in not_previously_forced:
                del forced_vertices[x]
            del forced_in_current[v][w],forced_in_current[w][v]
            if was_original:
                del forced_in_input[v][w],forced_in_input[w][v]

        actions.append(unforce)
        return remove_third_leg(v) and remove_third_leg(w) and \
            force_into_triangle(v,w) and force_into_triangle(w,v) and \
            force_from_triangle(v,w)

    def force_into_triangle(v,w):
        """
        After v,w has been added to forced edges, check if w
        belongs to a triangle, and if so force the opposite edge.
        Returns True if successful, False if found a contradiction.
        """
        if len(G[w]) != 3:
            return True
        x,y = [z for z in G[w] if z != v]
        if y not in G[x]:
            return True
        return force(x,y)

    def force_from_triangle(v,w):
        """
        After v,w has been added to forced edges, check whether it
        belongs to a triangle, and if so force the opposite edge.
        Returns True if successful, False if found a contradiction.
        """
        for u in list(G[v]):    # Use list to avoid dict changes
            if u in G[w]:
                if len(G[u]) < 3:
                    return len(G) == 3  # deg=2 only ok if 3 verts left
                x = [y for y in G[u] if y != v and y != w][0]
                if not force(u,x):
                    return False
        return True

    def contract(v):
        """
        Contract out degree two vertex.
        Returns True if cycle should be reported, False or None otherwise.
        Appends recursive search of contracted graph to action stack.
        """
        assert len(G[v]) == 2
        u,w = G[v]
        if w in G[u]:           # About to create parallel edge?
            if len(G) == 3:     # Graph is a triangle?
                return force(u,v) and force(v,w) and force(u,w)
            if not safely_remove(u,w):
                return None     # Unable to remove uw, no cycles exist

        if not force(u,v) or not force(v,w):
            return None     # Forcing the edges led to a contradiction
        remove(u,v)
        remove(v,w)
        G[u][w] = G[w][u] = False
        forced_in_current[u][w] = forced_in_current[w][u] = True
        del G[v],forced_vertices[v]

        def uncontract():
            del G[u][w],G[w][u]
            del forced_in_current[u][w],forced_in_current[w][u]
            forced_vertices[v] = True
            G[v] = {}

        actions.append(uncontract)
        if force_from_triangle(u,w):    # Contraction may have made a triangle
            actions.append(main)        # Search contracted graph recursively

    def handle_degree_two():
        """
        Handle case that the graph has a degree two vertex.
        Returns True if cycle should be reported, False or None otherwise.
        Appends recursive search of contracted graph to action stack.
        """
        v = degree_two.pop()
        def unpop():
            degree_two.append(v)
        actions.append(unpop)
        return contract(v)

    def main():
        """
        Main event dispatcher.
        Returns True if cycle should be reported, False or None otherwise.
        Appends recursive search of contracted graph to action stack.
        """
        if degree_two:
            return handle_degree_two()

        # At this point, we are going to branch, and if the time is really
        # exponential in the size of the remaining graph we can afford some
        # more expensive pruning steps first.

        # If graph is Hamiltonian it must be biconnected
        if not isBiconnected(G):
            return None

        # If graph is Hamiltonian, unforced edges must have a perfect matching.
        # We jump-start the matching algorithm with our previously computed
        # matching (or as much of it as fits the current graph) since that is
        # likely to be near-perfect.
        unforced = {v:{} for v in G}
        for v in G:
            for w in G[v]:
                if w not in forced_in_current[v]:
                    unforced[v][w] = True
        for v in list(previous_matching.keys()):
            if v not in unforced or previous_matching[v] not in unforced[v]:
                del previous_matching[v]
        M = matching(unforced, previous_matching)
        previous_matching.clear()
        previous_matching.update(M)
        if len(M) != len(G):
            return None

        # Here with a degree three graph in which the forced edges
        # form a matching.  Pick an unforced edge adjacent to a
        # forced one, if possible, else pick any unforced edge,
        # and branch on the chosen edge.
        if forced_vertices:
            v = arbitrary_item(forced_vertices)
        else:
            v = arbitrary_item(G)
        w = [x for x in G[v] if x not in forced_in_current[v]][0]

        def continuation():
            """Here after searching first recursive subgraph."""
            if force(v,w):
                actions.append(main)

        actions.append(continuation)
        if safely_remove(v,w):
            actions.append(main)

    # The main backtracking loop
    actions = [main]
    while actions:
        if actions.pop()():
            yield forced_in_input

# If run as "python CubicHam.py", run tests on various small graphs
# and check that the correct number of cycles is generated.

class CubicHamTest(unittest.TestCase):
    def check(self,G,N):
        """Make sure G has N Hamiltonian cycles."""
        count = 0
        for C in HamiltonianCycles(G):
            # Count the cycle.
            count += 1

            # Check that it's a degree-two undirected subgraph.
            for v in C:
                self.assertEqual(len(C[v]),2)
                for w in C[v]:
                    assert v in G and w in G[v] and v in C[w]

            # Check that it connects all vertices.
            nreached = 0
            x = arbitrary_item(G)
            a,b = x,x
            while True:
                nreached += 1
                a,b = b,[z for z in C[b] if z != a][0]
                if b == x:
                    break
            self.assertEqual(nreached,len(G))

        # Did we find enough cycles?
        self.assertEqual(count,N)

    def testCube(self):
        """Cube has six Hamiltonian cycles."""
        cube = {i:(i^1,i^2,i^4) for i in range(8)}
        self.check(cube,6)

    def twistedLadder(self,n):
        """Connect opposite vertices on an even length cycle."""
        return {i:((i+1)%n,(i-1)%n,(i+n//2)%n) for i in range(n)}

    def testEvenTwistedLadders(self):
        """twistedLadder(4n) has 2n+1 Hamiltonian cycles."""
        for n in range(4,50,4):
            self.check(self.twistedLadder(n),n//2+1)

    def testOddTwistedLadders(self):
        """twistedLadder(4n+2) has 2n+4 Hamiltonian cycles."""
        for n in range(6,50,4):
            self.check(self.twistedLadder(n),n//2+3)

    def truncate(self,G):
        """Replace each vertex of G by a triangle and return the result."""
        return {(v,w):{(v,u) for u in G[v] if u != w} | {(w,v)}
                for v in G for w in G[v]}

    def testSierpinski(self):
        """
        Sierpinski triangle like graphs formed by repeated truncation
        of K_4 should all have exactly three Hamiltonian cycles.
        """
        G = self.twistedLadder(4)   # Complete graph on four vertices
        for i in range(3):
            G = self.truncate(G)
            self.check(G,3)

if __name__ == "__main__":
    unittest.main()   

