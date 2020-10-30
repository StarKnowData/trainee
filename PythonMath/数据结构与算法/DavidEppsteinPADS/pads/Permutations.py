"""Permutations.py
Efficient recursive version of the Steinhaus-Johnson-Trotter algorithm
for listing all permutations of a set of items.
D. Eppstein, October 2011.

NOTE: The generators in this module work by making a sequence of
small changes to a permutation stored in a Python list object,
and then yielding that list. That means that the objects that they
generate (the list objects) must not be modified by their callers,
because that would break subsequent generation steps. And it also
means that each permutation yielded by the generator only has its
correct value up to the time the generator is called again, after
which this value will change. If you want to keep a persistent copy
of a permutation, or change it, you need to copy it into a
separate object. E.g.

    RIGHT:
        [list(p) for p in SteinhausJohnsonTrotter(n)]
        # makes a list of all the permutations of order n
    WRONG:
        list(SteinhausJohnsonTrotter(n))
        [p for p in SteinhausJohnsonTrotter(n)]
        # either way, these make a list of length n! all of whose
        # elements point to the same list object as each other

The Steinhaus-Johnson-Trotter implementation given here sets up a
sequence of recursive simple generators, each taking constant space,
for a total space of O(n), where n is the number of items being permuted.
The number of recursive calls to generate a swap that moves the item
originally in position n of the input permutation is O(n-i+1), so all
but a 1/n fraction of the swaps take no recursion and the rest always take O(n) time, for an average time per swap of O(1) and an average time per
generated permutation of O(1). The other generators are similar.
"""

import unittest

# 2to3 compatibility
try:
    xrange
except:
    xrange = range

def PlainChanges(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
    if n < 1:
        return
    up = xrange(n-1)
    down = xrange(n-2,-1,-1)
    recur = PlainChanges(n-1)
    try:
        while True:
            for x in down:
                yield x
            yield next(recur) + 1
            for x in up:
                yield x
            yield next(recur)
    except StopIteration:
        pass

def SteinhausJohnsonTrotter(x):
    """Generate all permutations of x.
    If x is a number rather than an iterable, we generate the permutations
    of range(x)."""

    # set up the permutation and its length
    try:
        perm = list(x)
    except:
        perm = list(range(x))
    n = len(perm)

    # run through the sequence of swaps
    yield perm
    for x in PlainChanges(n):
        perm[x],perm[x+1] = perm[x+1],perm[x]
        yield perm

def DoublePlainChanges(n):
    """Generate the swaps for double permutations."""
    if n < 1:
        return
    up = xrange(1,2*n-1)
    down = xrange(2*n-2,0,-1)
    recur = DoublePlainChanges(n-1)
    try:
        while True:
            for x in up:
                yield x
            yield next(recur) + 1
            for x in down:
                yield x
            yield next(recur) + 2
    except StopIteration:
        pass

def DoubleSteinhausJohnsonTrotter(n):
    """Generate all double permutations of the range 0 through n-1"""
    perm = []
    for i in range(n):
        perm += [i,i]

    # run through the sequence of swaps
    yield perm
    for x in DoublePlainChanges(n):
        perm[x],perm[x+1] = perm[x+1],perm[x]
        yield perm

def StirlingChanges(n):
    """Variant Steinhaus-Johnson-Trotter for Stirling permutations.
    A Stirling permutation is a double permutation in which each
    pair of values has only larger values between them.
    The algorithm is to sweep the largest pair of values through
    the sequence of smaller values, recursing when it reaches
    the ends of the sequence, exactly as in the standard
    Steinhaus-Johnson-Trotter algorithm. However, it differs
    in swapping items two positions apart instead of adjacent items."""
    if n <= 1:
        return
    up = xrange(2*n-2)
    down = xrange(2*n-3,-1,-1)
    recur = StirlingChanges(n-1)
    try:
        while True:
            for x in down:
                yield x
            yield next(recur) + 2
            for x in up:
                yield x
            yield next(recur)
    except StopIteration:
        pass

def StirlingPermutations(n):
    """Generate all Stirling permutations of order n."""
    perm = []
    for i in range(n):
        perm += [i,i]

    # run through the sequence of swaps
    yield perm
    for x in StirlingChanges(n):
        perm[x],perm[x+2] = perm[x+2],perm[x]
        yield perm

def InvolutionChanges(n):
    """Generate change sequence for involutions on n items.
    Uses a variation of the Steinhaus-Johnson-Trotter idea,
    in which we first recurse for n-1, generating involutions
    in which the last item is fixed, and then we the match
    for the last item back and forth over a recursively
    generated sequence for n-2."""
    if n <= 3:
        for c in [[],[],[0],[0,1,0]][n]:
            yield c
        return
    for c in InvolutionChanges(n-1):
        yield c
    yield n-2
    for i in range(n-4,-1,-1):
        yield i
    ic = InvolutionChanges(n-2)
    up = range(0,n-2)
    down = range(n-3,-1,-1)
    try:
        while True:
            yield next(ic) + 1
            for i in up:
                yield i
            yield next(ic)
            for i in down:
                yield i
    except StopIteration:
        yield n-4

def Involutions(n):
    """Generate involutions on n items.
    The first involution is always the one in which all items
    are mapped to themselves, and the last involution is the one
    in which only the final two items are swapped.
    Each two involutions differ by a change that either adds or
    removes an adjacent pair of swapped items, moves a swap target
    by one, or swaps two adjacent swap targets."""
    p = list(range(n))
    yield p
    for c in InvolutionChanges(n):
        x,y = p[c],p[c+1]   # current partners of c and c+1
        if x == c and y != c+1: x = c+1
        if x != c and y == c+1: y = c
        p[x],p[y],p[c],p[c+1] = c+1, c, y, x    # swap partners
        yield p

# If run standalone, perform unit tests
class PermutationTest(unittest.TestCase):    
    def testChanges(self):
        """Do we get the expected sequence of changes for n=3?"""
        self.assertEqual(list(PlainChanges(3)),[1,0,1,0,1])
    
    def testLengths(self):
        """Are the lengths of the generated sequences factorial?"""
        f = 1
        for i in range(2,7):
            f *= i
            self.assertEqual(f,len(list(SteinhausJohnsonTrotter(i))))
    
    def testDistinct(self):
        """Are all permutations in the sequence different from each other?"""
        for i in range(2,7):
            s = set()
            n = 0
            for x in SteinhausJohnsonTrotter(i):
                s.add(tuple(x))
                n += 1
            self.assertEqual(len(s),n)
    
    def testAdjacent(self):
        """Do consecutive permutations in the sequence differ by a swap?"""
        for i in range(2,7):
            last = None
            for p in SteinhausJohnsonTrotter(i):
                if last:
                    diffs = [j for j in range(i) if p[j] != last[j]]
                    self.assertEqual(len(diffs),2)
                    self.assertEqual(p[diffs[0]],last[diffs[1]])
                    self.assertEqual(p[diffs[1]],last[diffs[0]])
                last = list(p)
    
    def testListInput(self):
        """If given a list as input, is it the first output?"""
        for L in ([1,3,5,7], list('zyx'), [], [[]], list(range(20))):
            self.assertEqual(L,next(SteinhausJohnsonTrotter(L)))

    def testInvolutions(self):
        """Are these involutions and do we have the right number of them?"""
        telephone = [1,1,2,4,10,26,76,232,764]
        for n in range(len(telephone)):
            count = 0
            sorted = list(range(n))
            invs = set()
            for p in Involutions(n):
                self.assertEqual([p[i] for i in p],sorted)
                invs.add(tuple(p))
                count += 1
            self.assertEqual(len(invs),count)
            self.assertEqual(len(invs),telephone[n])

if __name__ == "__main__":
    unittest.main()
