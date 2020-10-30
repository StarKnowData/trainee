"""Bipartite.py

Two-color graphs and find related structures.
D. Eppstein, May 2004.
"""

import unittest
from Biconnectivity import BiconnectedComponents
import Graphs
import DFS

class NonBipartite(Exception):
    pass

def TwoColor(G):
    """
    Find a bipartition of G, if one exists.
    Raises NonBipartite or returns dict mapping vertices
    to two colors (True and False).
    """
    color = {}
    for v,w,edgetype in DFS.search(G):
        if edgetype is DFS.forward:
            color[w] = not color.get(v,False)
        elif edgetype is DFS.nontree and color[v] == color[w]:
            raise NonBipartite
    return color

def Bipartition(G):
    """
    Find a bipartition of G, if one exists.
    Raises NonBipartite or returns sequence of vertices
    on one side of the bipartition.
    """
    color = TwoColor(G)
    for v in color:
        if color[v]:
            yield v

def isBipartite(G):
    """
    Return True if G is bipartite, False otherwise.
    """
    try:
        TwoColor(G)
        return True
    except NonBipartite:
        return False

def BipartiteOrientation(G,adjacency_list_type=set):
    """
    Given an undirected bipartite graph G, return a directed graph in which
    the edges are oriented from one side of the bipartition to the other.
    The second argument has the same meaning as in Graphs.copyGraph.
    """
    B = Bipartition(G)
    return {v:adjacency_list_type(iter(G[v])) for v in B}

def OddCore(G):
    """
    Subgraph of vertices and edges that participate in odd cycles.
    Aka, the union of nonbipartite biconnected components.
    """
    return Graphs.union(*[C for C in BiconnectedComponents(G)
                          if not isBipartite(C)])

# If run as "python Bipartite.py", run tests on various small graphs
# and check that the correct results are obtained.

class BipartitenessTest(unittest.TestCase):
    def cycle(self,n):
        return {i:[(i-1)%n,(i+1)%n] for i in range(n)}

    def testEvenCycles(self):
        for i in range(4,12,2):
            self.assertEqual(isBipartite(self.cycle(i)), True)

    def testOddCycles(self):
        for i in range(3,12,2):
            self.assertEqual(isBipartite(self.cycle(i)), False)

if __name__ == "__main__":
    unittest.main()   

