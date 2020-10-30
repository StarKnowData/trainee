"""AcyclicReachability.py

Bit-parallel algorithm for testing which vertices can reach which other vertices in a DAG.

Usage:
    R = Reachability(G)
    ...
    R.reachable(source,destination)
returns a boolean value: True if G contains a path from the source vertex
to the destination vertex, and False otherwise. The initialization of R
performs a linear number of bitvector operations, after which each reachability
test takes constant time to perform.

D. Eppstein, April 2009.
"""

import unittest
from PartialOrder import TopologicalOrder

class Reachability:
    def __init__(self,G):
        """Initialize a reachability data structure for the given DAG."""
        self.key = {}
        self.canReach = []
        L = TopologicalOrder(G)
        L.reverse()
        for v in L:
            k = self.key[v] = len(self.canReach)
            bits = 1<<k
            for w in G[v]:
                bits |= self.canReach[self.key[w]]
            self.canReach.append(bits)

    def reachable(self,source,destination):
        """Test whether the DAG has a path from source to destination."""
        return (1<<self.key[destination])&self.canReach[self.key[source]] != 0

class ReachabilityTest(unittest.TestCase):
    def testReachable(self):
        G = {"A":["C"],"B":["C","D"],"C":["D","E"],"D":[],"E":[]}
        R = Reachability(G)
        for s in "ABCDE":
            for t in "ABCDE":
                self.assertEqual(R.reachable(s,t),
                                 s <= t and s+t not in ["AB","DE"])

if __name__ == "__main__":
    unittest.main()   
