"""Eratosthenes.py
Space-efficient version of sieve of Eratosthenes.
D. Eppstein, May 2004.

The main storage of the algorithm is a hash table D with sqrt(n)
nonempty entries for a total of O(sqrt n) space.

At any point in the algorithm, each prime p occupies a cell with key at
most 2n.  E.g. by Bertrand's postulate, there is another prime p'
between n/p and 2n/p, and p' can not yet have been included because it
is greater than sqrt n, so key pp' can not be used by any other prime;
therefore p is placed at or before key pp'<2n.  Thus, the number of
times p can have been moved from its initial placement at p^2 is < n/p.
The time for the algorithm, up to output n, is O(n) + sum_{prime p <=
sqrt(n)} O(n/p) = O(n log log n).  The algorithm also makes a recursive
call, but the recursion only generates primes up to sqrt n so its time
and space is negligible compared to the outer call.

If efficiency is a significant concern it may be better to combine
this idea with segmentation and bitvectors, as in the code by
T. Oliveira e Silva at http://www.ieeta.pt/~tos/software/prime_sieve.html
Thanks to Alex Martelli for the suggestion of keeping one prime
per entry of D, rather than a list of all prime factors of D.

We also include a variant of the sieve that produces a list of all
integers, with their factorizations, and an application of this
variant in the generation of practical numbers.
"""

import unittest
from collections import defaultdict

def primes():
    '''Yields the sequence of primes via the Sieve of Eratosthenes.'''
    yield 2                 # Only even prime.  Sieve only odd numbers.

    # Generate recursively the sequence of primes up to sqrt(n).
    # Each p from the sequence is used to initiate sieving at p*p.
    roots = primes()
    root = next(roots)
    square = root*root

    # The main sieving loop.
    # We use a hash table D such that D[n]=2p for p a prime factor of n.
    # Each prime p up to sqrt(n) appears once as a value in D, and is
    # moved to successive odd multiples of p as the sieve progresses.
    D = {}
    n = 3
    while True:
        if n >= square:     # Time to include another square?
            D[square] = root+root
            root = next(roots)
            square = root*root

        if n not in D:      # Not witnessed, must be prime.
            yield n
        else:               # Move witness p to next free multiple.
            p = D[n]
            q = n+p
            while q in D:
                q += p
            del D[n]
            D[q] = p
        n += 2              # Move on to next odd number.

def FactoredIntegers():
    """
    Generate pairs n,F where F is the prime factorization of n.
    F is represented as a dictionary in which each prime factor of n
    is a key and the exponent of that prime is the corresponding value.
    """
    yield 1,{}
    i = 2
    factorization = defaultdict(dict)
    while True:
        if i not in factorization:  # prime
            F = {i:1}
            yield i,F
            factorization[2*i] = F
        elif len(factorization[i]) == 1:    # prime power
            p,x = next(iter(factorization[i].items()))
            F = {p:x+1}
            yield i,F
            factorization[2*i] = F
            factorization[i+p**x][p] = x
            del factorization[i]
        else:
            yield i,factorization[i]
            for p,x in factorization[i].items():
                q = p**x
                iq = i+q
                if iq in factorization and p in factorization[iq]:
                    iq += p**x  # skip higher power of p
                factorization[iq][p] = x
            del factorization[i]
        i += 1

def MoebiusSequence():
    """The sequence of values of the Moebius function, OEIS A008683."""
    for n,F in FactoredIntegers():
        if n > 1 and set(F.values()) != {1}:
            yield 0
        else:
            yield (-1)**len(F)

MoebiusFunctionValues = [None]
MoebiusFunctionIterator = MoebiusSequence()
def MoebiusFunction(n):
    """A functional version of the Moebius sequence.
    Efficient only for small values of n."""
    while n >= len(MoebiusFunctionValues):
        MoebiusFunctionValues.append(next(MoebiusFunctionIterator))
    return MoebiusFunctionValues[n]

def isPracticalFactorization(f):
    """Test whether f is the factorization of a practical number."""
    f = sorted(f.items())
    sigma = 1
    for p,x in f:
        if sigma < p - 1:
            return False
        sigma *= (p**(x+1)-1)//(p-1)
    return True

def PracticalNumbers():
    """Generate the sequence of practical (or panarithmic) numbers."""
    for x,f in FactoredIntegers():
        if isPracticalFactorization(f):
            yield x

# If run standalone, perform unit tests
class SieveTest(unittest.TestCase):    
    def testPrime(self):
        """Test that the first few primes are generated correctly."""
        G = primes()
        for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
            self.assertEqual(p,next(G))

    def testPractical(self):
        """Test that the first few practical nos are generated correctly."""
        G = PracticalNumbers()
        for p in [1,2,4,6,8,12,16,18,20,24,28,30,32,36]:
            self.assertEqual(p,next(G))

if __name__ == "__main__":
    unittest.main()
