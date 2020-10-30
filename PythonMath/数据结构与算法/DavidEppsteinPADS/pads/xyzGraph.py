"""xyzGraph.py

An xyz graph is the graph formed by a set of points in R^3 such that any
axis-parallel line intersects the set in zero or two points; we add an edge
for the two points on any nonempty line. These graphs include all bipartite
simple polyhedra, as well as some other nonplanar graphs; see
http://11011110.livejournal.com/tag/xyz+graphs for more.

We implement here an exponential-time algorithm for finding such
representations of an arbitrary graph, when they exist.

D. Eppstein, June 2006.
"""

from Graphs import isUndirected
from PartialOrder import TopologicalOrder
from StrongConnectivity import StronglyConnectedComponents
from Biconnectivity import stOrientation
import unittest
from collections import defaultdict

# 2to3 compatibility
try:
    xrange
except:
    xrange = range

def CubicMatchPartitions(G):
    """Partition a biconnected cubic graph G into three matchings.
    Each matching is represented as a graph, in which G[v] is a list
    of the three edges of G in the order of the three matchings.
    This function generates a sequence of such representations.
    """
    
    if not isUndirected(G):
        raise ValueError("CubicMatchPartitions: graph is not undirected")
    for v in G:
        if len(G[v]) != 3:
            raise ValueError("CubicMatchPartitions: graph is not cubic")
    ST = stOrientation(G)
    L = TopologicalOrder(ST)
    for B in xrange(1<<(len(L)//2 - 1)):
        # Here with a bitstring representing the sequence of choices
        out = {}
        pos = 0
        for v in L:
            source = [w for w in G[v] if w in out]
            sourcepos = {}
            adjlist = [None,None,None]
            for w in source:
                sourcepos[w] = [i for i in (0,1,2) if out[w][i]==v][0]
                adjlist[sourcepos[w]] = w
            usedpos = [sourcepos[w] for w in source]
            if len(set(usedpos)) != len(usedpos):
                # two edges in with same index, doesn't form matching
                break 
            elif len(source) == 0:
                # start vertex, choose one orientation
                adjlist = list(ST[v])
            elif len(source) == 1:
                # two outgoing vertices, one incoming
                avail = [i for i in (0,1,2) if i != usedpos[0]]
                if B & (1<<pos):
                    avail.reverse()
                pos += 1
                for i,w in zip(avail,list(ST[v])):
                    adjlist[i] = w
            elif len(source) == 2:
                avail = 3 - sum(usedpos)
                adjlist[avail] = list(ST[v])[0]
            out[v] = adjlist
            if len(source) == 3:
                # final vertex of topological ordering, still all consistent
                yield out
                
def groupByCycles(G,i,j):
    """
    Collect cycles of G[v][i] and G[v][j] edges,
    return a dictionary mapping v to the number of its cycle.
    """
    G = {v:(G[v][i],G[v][j]) for v in G}
    index = 0
    D = {}
    for C in StronglyConnectedComponents(G):
        for v in C:
            D[v] = index
        index += 1
    return D

def isxyz(points):
    """
    True if there are two points per axis-parallel line, False otherwise.
    """
    for i,j in [(0,1),(0,2),(1,2)]:
        projections = defaultdict(list)
        for p in points:
            projections[p[i],p[j]].append(p)
        for L in projections.values():
            if len(L) != 2:
                return False
    return True
        

def xyzEmbeddings(G):
    """
    List all xyz graph embeddings of G.
    Each is returned as a dictionary mapping vertices to triples of points.
    To get just the points, use D.values().
    """
    for G in CubicMatchPartitions(G):
        xyz = [groupByCycles(G,i,j) for i,j in [(0,1),(0,2),(1,2)]]
        xyz = {v:[xyz[i][v] for i in (0,1,2)] for v in G}
        if isxyz(list(xyz.values())):
            yield xyz

class xyzGraphTest(unittest.TestCase):
    cube = {v:[v^i for i in (1,2,4)] for v in range(8)}

    def testCubicMatchPartitions(self):
        """Check that a cube has the right number of matching partitions."""
        self.assertEqual(len(list(CubicMatchPartitions(self.cube))),4)

    def testCubeIsXYZ(self):
        """Check that a cube is correctly identified as an xyz graph."""
        self.assertEqual(len(list(xyzEmbeddings(self.cube))),1)

if __name__ == "__main__":
    unittest.main()   

