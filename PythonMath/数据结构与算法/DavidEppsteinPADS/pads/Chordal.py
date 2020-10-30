"""Chordal.py

Recognize and compute elimination ordering of chordal graphs, using
an algorithm from Habib, McConnell, Paul, and Viennot, "Lex-BFS and
Partition Refinement, with Applications to Transitive Orientation,
Interval Graph Recognition, and Consecutive Ones Testing", Theor.
Comput. Sci. 234:59-84 (2000), http://www.cs.colostate.edu/~rmm/lexbfs.ps

D. Eppstein, November 2003.
"""

import unittest
from LexBFS import LexBFS
from Graphs import isUndirected

def PerfectEliminationOrdering(G):
    """Return a perfect elimination ordering, or raise an exception if not chordal.
    G should be represented in such a way that "for v in G" loops through
    the vertices, and "G[v]" produces a list of the neighbors of v; for
    instance, G may be a dictionary mapping each vertex to its neighbor set.
    Running time is O(n+m) and additional space usage over G is O(n+m).
    """
    alreadyProcessed = set()
    B = list(LexBFS(G))
    position = {B[i]:i for i in range(len(B))}
    leftNeighbors = {}
    parent = {}
    for v in B:
        leftNeighbors[v] = set(G[v]) & alreadyProcessed
        alreadyProcessed.add(v)
        if leftNeighbors[v]:
            parent[v] = B[max([position[w] for w in leftNeighbors[v]])]
            if not leftNeighbors[v] - {parent[v]} <= leftNeighbors[parent[v]]:
                raise ValueError("Input to PerfectEliminationOrdering is not chordal")
    B.reverse()
    return B

def Chordal(G):
    """Test if a given graph is chordal."""
    if not isUndirected(G):
        raise ValueError("Input to Chordal is not an undirected graph")
    try:
        PerfectEliminationOrdering(G)
    except:
        return False
    return True

class ChordalTest(unittest.TestCase):
    claw = {0:[1,2,3],1:[0],2:[0],3:[0]}
    butterfly = {0:[1,2,3,4],1:[0,2],2:[0,1],3:[0,4],4:[0,3]}
    diamond = {0:[1,2],1:[0,2,3],2:[0,1,3],3:[1,2]}
    quad = {0:[1,3],1:[0,2],2:[1,3],3:[0,2]}
    graphs = [(claw,True), (butterfly,True), (diamond,True), (quad,False)]
    
    def testChordal(self):
        """Check that Chordal() returns the correct answer on each test graph."""
        for G,isChordal in ChordalTest.graphs:
            self.assertEqual(Chordal(G), isChordal)

    def testElimination(self):
        """Check that PerfectEliminationOrdering generates an elimination ordering."""
        for G,isChordal in ChordalTest.graphs:
            if isChordal:
                eliminated = set()
                for v in PerfectEliminationOrdering(G):
                    eliminated.add(v)
                    for w in G[v]:
                        for x in G[v]:
                            if w != x and w not in eliminated and x not in eliminated:
                                self.assertTrue(w in G[x] and x in G[w]) 

if __name__ == "__main__":
    unittest.main()   
