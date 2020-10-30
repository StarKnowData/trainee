"""OrderedSequence.py

Classes for sequences of items subject to insertions and deletions,
with fast comparisons of the positions of two items in a sequence.

D. Eppstein, November 2003.
"""

import sys
from Sequence import Sequence

class SimpleOrderedSequence(Sequence):
    """Maintain a sequence of items subject to insertions, removals,
    and comparisons of the positions of pairs of items.  In addition to
    the information stored for a Sequence, we store an integer tag
    for each item, with the order of tags the same as the sequence order.
    When two tags collide, we renumber the whole sequence; this behavior
    can be changed by overriding the rebalance method.  Renumbers happen
    infrequently (roughly one in every log(sys.maxint) insertions)
    but take time proportional to the number of items, so it is preferable
    to use this data structure only for sequences of very few items.
    """

    def __init__(self,iterable=[],key=None):
        """The only additional data we maintain over a vanilla Sequence
        is a dictionary self._tag mapping sequence items to integers,
        such that an item is earlier than another iff its tag is smaller.
        """
        self._tag = {}
        Sequence.__init__(self,iterable,key=key)

    def cmp(self,x,y):
        """Compare the positions of x and y in the sequence."""
        return cmp(self._tag[self.key(x)],self._tag[self.key(y)])

    def append(self,x):
        """Add x to the end of the sequence."""
        if not self._next:  # add to empty sequence
            Sequence.append(self,x)
            self._tag[self.key(x)] = sys.maxint//2
        else:
            self.insertAfter(self._prev[self._first],x)

    def insertAfter(self,x,y):
        """Add y after x and compute a tag for it."""
        Sequence.insertAfter(self,x,y)
        x = self.key(x)
        y = self.key(y)
        next = self._next[y]
        if next == self._first:
            nexttag = sys.maxint
        else:
            nexttag = self._tag[next]
        xtag = self._tag[x]
        self._tag[y] = xtag + (nexttag - xtag + 1)//2
        if self._tag[y] == nexttag:
            self.rebalance(y)

    def insertBefore(self,x,y):
        """Add y before x in the sequence."""
        Sequence.insertBefore(self,x,y)
        x = self.key(x)
        y = self.key(y)
        if self._first == y:
            self._tag[y] = self._tag[x]//2
            if self._tag[y] == self._tag[x]:
                self.rebalance(y)

    def rebalance(self,x):
        """Clean up after x and its successor's tags collide."""
        base = 0
        increment = sys.maxint//len(self)
        for y in self:
            self._tag[y] = base
            base += increment

class LogarithmicOrderedSequence(SimpleOrderedSequence):
    """Maintain a sequence of items subject to insertions, removals,
    and comparisons of the positions of pairs of items.  We use the
    method of Bender, et al, ``Two Simplified Algorithms for Maintaining
    Order in a List,'' ESA 2002 (LNCS #2461) pp. 152-164,
    http://theory.lcs.mit.edu/~edemaine/papers/DietzSleator_ESA2002/
    Due to rebalancing on the integer tags used to maintain order,
    the amortized time per insertion in an n-item list is O(log n).
    """

    def rebalance(self,x):
        """Clean up after x and its successor's tags collide.

        At each iteration of the rebalancing algorithm, we look at
        a contiguous subsequence of items, defined as the items for which
        self._tag &~ mask == base.  We keep track of the first and last
        items in the subsequence, and the number of items, until we find
        a subsequence with sufficiently low density, at which point
        we space the tags evenly throughout the available values.

        The multiplier controls the growth of the threshhold density;
        it is 2/T for the T parameter described by Bender et al.
        Large multipliers lead to fewer relabels, while small items allow
        us to handle more items with machine integer tags, so we vary the
        multiplier dynamically to allow it to be as large as possible
        without producing integer overflows.
        """
        base = self._tag[x]
        mask = 0
        threshhold = 1.0
        first = last = x
        nItems = 1
        multiplier = 2/(2*len(self))**(1/30.)
        while 1:
            while first != self._first and \
                    self._tag[self._prev[first]] &~ mask == base:
                first = self._prev[first]
                nItems += 1
            while self._next[last] != self._first and \
                    self._tag[self._next[last]] &~ mask == base:
                last = self._next[last]
                nItems += 1
            increment = (mask+1)//nItems
            if increment >= threshhold:     # found rebalanceable range
                item = first
                while item != last:
                    self._tag[item] = base
                    item = self._next[item]
                    base += increment
                self._tag[last] = base
                return
            mask = (mask << 1) + 1          # expand to next power of two
            base = base &~ mask
            threshhold *= multiplier
