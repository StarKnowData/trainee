"""SortedSet.py

Set data structure augmented by a method to list all items in the set in sorted order.

Two naive methods to do this would be
  (1) just use a Python set type and sort when requested, or
  (2) use a skip list or balanced binary search tree to store the items.
Our solution is almost as simple as (1) but has the same amortized
efficiency as (2): store a list of the items in the sorted order they
were most recently output as, together with small lists of the changes
to the set since then, and handle requests to list all items by
sorting the change lists and merging with the larger sorted list.

D. Eppstein, August 2008.
"""

from itertools import chain
from functools import cmp_to_key

class SortedSet:
    """Maintain a set of items in such a way that iter(set) returns the items in sorted order.
    We also allow a custom comparison routine, and augment the usual add() and remove() methods
    with an update() method that tells the set that a single item's position in the order might
    have changed."""
    
    def __init__(self,iterable=[],comparison=None):
        """Create a new sorted set with the given comparison function."""
        self._comparison = comparison
        self._set = set(iterable)
        self._previous = None

    def __len__(self):
        """How many items do we have?"""
        return len(self._set)

    def add(self,item):
        """Add the given item to a sorted set."""
        self._set.add(item)
        if self._previous:
            self._additions.add(item)

    def remove(self,item):
        """Remove the given item from a sorted set."""
        self._set.remove(item)
        if self._previous:
            self._removals.add(item)
            self._additions.discard(item)

    def update(self,item):
        """Flag the given item as needing re-comparison with its neighbors in the order."""
        if self._previous:
            self._removals.add(item)
            self._additions.add(item)

    def __iter__(self):
        if not self._previous:
            sortarg = self._set
        else:
            sortarg = chain(self._additions,
                            (x for x in self._previous
                             if x not in self._removals))
        if self._comparison:
            self._previous = sorted(sortarg,key=cmp_to_key(self._comparison))
        else:
            self._previous = sorted(sortarg)
        self._removals = set()
        self._additions = set()
        return iter(self._previous)

# ======================================================================
#   Unit tests
# ======================================================================

if __name__ == "__main__":
    import unittest

    class SortedSetTest(unittest.TestCase):
        def testSortedSet(self):
            """Test whether SortedSet works correctly."""
            S = SortedSet()
            self.assertEqual(len(S),0)
            S.add(1)
            S.add(4)
            S.add(2)
            S.add(9)
            S.add(3)
            self.assertEqual(list(S),[1,2,3,4,9])
            self.assertEqual(len(S),5)
            S.remove(4)
            S.add(6)
            S.add(5)
            S.add(7)
            S.remove(6)
            S.remove(1)
            S.remove(2)
            S.add(1)
            self.assertEqual(list(S),[1,3,5,7,9])
            self.assertEqual(list(SortedSet([1,3,6,7])),[1,3,6,7])

    unittest.main()   
