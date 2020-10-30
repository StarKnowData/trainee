"""IntegerHeap.py

Priority queues of integer keys based on van Emde Boas trees.
Only the keys are stored; caller is responsible for keeping
track of any data associated with the keys in a separate dictionary.

We use a version of vEB trees in which all accesses to subtrees
are performed indirectly through a hash table and the data structures
for the subtrees are only created when they are nonempty. As a
consequence, the data structure takes only linear space
(linear in the number of keys stored in the heap) while still preserving
the O(log log U) time per operation of vEB trees. For better performance,
we switch to bitvectors for sufficiently small integer sizes.

Usage:
    Q = BitVectorHeap() # Bit-vector based heap for integers
    Q = FlatHeap(i)     # Flat heap for 2^i-bit integers
    Q = LinearHeap()    # Set-based heap with linear-time min operation
    Q = IntegerHeap(i)  # Choose between BVH and FH depending on i
    Q.add(x)            # Include x among the values in the heap
    Q.remove(x)         # Remove x from the values in the heap
    Q.min()             # Return the minimum value in the heap
    if Q                # True if Q is nonempty, false if empty

Because the min operation in LinearHeap is a Python primitive rather than
a sequence of interpreted Python instructions, it is actually quite fast;
testing indicates that, for 32-bit keys, FlatHeap(5) beats LinearHeap only
for heaps of 250 or more items. This breakeven point would likely be
different for different numbers of bits per word or when runtime optimizers
such as psyco are in use.

D. Eppstein, January 2010
"""

def IntegerHeap(i):
    """Return an integer heap for 2^i-bit integers.
    We use a BitVectorHeap for small i and a FlatHeap for large i.
    
    Timing tests indicate that the cutoff i <= 3 is slightly
    faster than the also-plausible cutoff i <= 2, and that both
    are much faster than the way-too-large cutoff i <= 4.
    The resulting IntegerHeap objects will use 255-bit long integers,
    still small compared to the overhead of a FlatHeap."""
    if i <= 3:
        return BitVectorHeap()
    return FlatHeap(i)

Log2Table = {}          # Table of powers of two, with their logs
def Log2(b):
    """Return log_2(b), where b must be a power of two."""
    while b not in Log2Table:
        i = len(Log2Table)
        Log2Table[1<<i] = i
    return Log2Table[b]

# ======================================================================
#   BitVectorHeap
# ======================================================================

class BitVectorHeap:
    """Maintain the minimum of a set of integers using bitvector operations."""
    def __init__(self):
        """Create a new BitVectorHeap."""
        self._S = 0
        
    def __nonzero__(self):
        """True if this heap is nonempty, false if empty."""
        return self._S != 0
        
    def __bool__(self):
        """True if this heap is nonempty, false if empty."""
        return self._S != 0

    def add(self,x):
        """Include x among the values in the heap."""
        self._S |= 1<<x

    def remove(self,x):
        """Remove x from the values in the heap."""
        self._S &=~ 1<<x

    def min(self):
        """Return the minimum value in the heap."""
        if not self._S:
            raise ValueError("BitVectorHeap is empty")
        return Log2(self._S &~ (self._S - 1))

# ======================================================================
#   FlatHeap
# ======================================================================

class FlatHeap:
    """Maintain the minimum of a set of 2^i-bit integer values."""
    def __init__(self,i):
        """Create a new FlatHeap for 2^i-bit integers."""
        self._min = None
        self._order = i
        self._shift = (1 << (i - 1))
        self._max = (1 << (1 << i)) - 1
        self._HQ = IntegerHeap(i-1) # Heap of high halfwords
        self._LQ = {}               # Map high half to heaps of low halfwords

    def _rangecheck(self,x):
        """Make sure x is a number we can include in this FlatHeap."""
        if x < 0 or x > self._max:
            raise ValueError("FlatHeap: %s out of range" % repr(x))

    def __nonzero__(self):
        """True if this heap is nonempty, false if empty."""
        return not (self._min is None)

    def __bool__(self):
        """True if this heap is nonempty, false if empty."""
        return not (self._min is None)

    def min(self):
        """Return the minimum value in the heap."""
        if self._min is None:
            raise ValueError("FlatHeap is empty")
        return self._min

    def add(self,x):
        """Include x among the values in the heap."""
        self._rangecheck(x)
        if self._min is None or self._min == x:
            # adding to an empty heap is easy
            self._min = x
            return
        if x < self._min:
            # swap to make sure the value we're adding is non-minimal
            x, self._min = self._min, x
        H = x >> self._shift            # split into high and low halfwords
        L = x - (H << self._shift)
        if H not in self._LQ:
            self._HQ.add(H)
            self._LQ[H] = IntegerHeap(self._order-1)
        self._LQ[H].add(L)

    def remove(self,x):
        """Remove x from the values in the heap."""
        self._rangecheck(x)
        if self._min == x:
            # Removing minimum, move next value into place
            # and prepare to remove that next value from secondary heaps
            if not self._HQ:
                self._min = None
                return
            H = self._HQ.min()
            L = self._LQ[H].min()
            x = self._min = (H << self._shift) + L
        else:
            H = x >> self._shift            # split into high and low halfwords
            L = x - (H << self._shift)
        if H not in self._LQ:
            return                          # ignore removal when not in heap
        self._LQ[H].remove(L)
        if not self._LQ[H]:
            del self._LQ[H]
            self._HQ.remove(H)

# ======================================================================
#   LinearHeap
# ======================================================================


class LinearHeap:
    """Maintain the minimum of a set of integers using a set object."""
    def __init__(self):
        """Create a new BitVectorHeap."""
        self._S = set()
        
    def __nonzero__(self):
        """True if this heap is nonempty, false if empty."""
        return len(self._S) > 0
        
    def __bool__(self):
        """True if this heap is nonempty, false if empty."""
        return len(self._S) > 0

    def add(self,x):
        """Include x among the values in the heap."""
        self._S.add(x)

    def remove(self,x):
        """Remove x from the values in the heap."""
        self._S.remove(x)

    def min(self):
        """Return the minimum value in the heap."""
        return min(self._S)


# ======================================================================
#   Unit tests
# ======================================================================

if __name__ == "__main__":
    import unittest,random
    random.seed(1234)

    class IntegerHeapTest(unittest.TestCase):
        def testHeaps(self):
            o = 5               # do tests on 2^5-bit integers
            N = LinearHeap()
            I = IntegerHeap(o)
            for iteration in range(20000):
                self.assertEqual(bool(N),bool(I))   # both have same emptiness
                if (not N) or random.randrange(2):  # flip coin for add/remove
                    x = random.randrange(1<<(1<<o))
                    N.add(x)
                    I.add(x)
                else:
                    x = N.min()
                    self.assertEqual(x,I.min())
                    N.remove(x)
                    I.remove(x)

    unittest.main()   
