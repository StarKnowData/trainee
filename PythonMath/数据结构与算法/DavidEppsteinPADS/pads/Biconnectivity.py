"""Biconnectivity.py

DFS-based algorithm for computing biconnected components.

D. Eppstein, April 2004.
"""

import unittest
from Graphs import isUndirected
from Util import arbitrary_item
from PartialOrder import TopologicalOrder

import DFS

disconnected = object() # flag for BiconnectedComponents

class BiconnectedComponents(DFS.Searcher):
    """
    Generate the biconnected components of G.  G should be represented in
    such a way that "for v in G" loops through the vertices, and "G[v]"
    produces a list of the neighbors of v; for instance, G may be a
    dictionary mapping each vertex to its neighbor set.
    The result of BiconnectedComponents(G) is a sequence of subgraphs of G.
    """

    def __init__(self,G):
        """Search for biconnected components of graph G."""
        if not isUndirected(G):
            raise ValueError("BiconnectedComponents: input not undirected graph")

        # set up data structures for DFS
        self._components = []
        self._dfsnumber = {}
        self._activelen = {}
        self._active = []
        self._low = {}
        self._ancestors = {} # directed subgraph from nodes to DFS ancestors

        # perform the Depth First Search
        DFS.Searcher.__init__(self,G)

        # clean up now-useless data structures
        del self._dfsnumber, self._activelen, self._active
        del self._low, self._ancestors

    def __iter__(self):
        """Return iterator for sequence of biconnected components."""
        return iter(self._components)

    def preorder(self,parent,child):
        if parent == child:
            self._active = [child]
        else:
            self._active.append(child)
        self._low[child] = self._dfsnumber[child] = len(self._dfsnumber)
        self._ancestors[child] = set()
        self._activelen[child] = len(self._active)

    def backedge(self,source,destination):
        if self._dfsnumber[destination] < self._dfsnumber[source]:
            self._low[source] = min(self._low[source],
                                    self._dfsnumber[destination])
            self._ancestors[source].add(destination)

    def postorder(self,parent,child):
        if self._low[child] != self._dfsnumber[parent]:
            self._low[parent] = min(self._low[parent],self._low[child])
            self._activelen[parent] = len(self._active)
        elif parent != child:
            self._component(self._activelen[parent],parent)
        elif not self._components or child not in self._components[-1]:
            self._component()

    def _component(self,start=0, articulation_point=disconnected):
        """Make new component, removing active vertices from start onward."""
        component = {}
        if articulation_point is not disconnected:
            component[articulation_point] = set()
        for v in self._active[start:]:
            component[v] = set()
            for w in self._ancestors[v]:
                component[v].add(w)
                component[w].add(v)
        del self._active[start:]
        self._components.append(component)


class NotBiconnected(Exception): pass

class BiconnectivityTester(DFS.Searcher):
    """
    Stripped down version of BiconnectedComponents.
    Either successfully inits or raises NotBiconnected.
    Otherwise does nothing.
    """

    def __init__(self,G):
        """Search for biconnected components of graph G."""
        if not isUndirected(G):
            raise NotBiconnected
        self._dfsnumber = {}
        self._low = {}
        self._rootedge = None
        DFS.Searcher.__init__(self,G)

    def preorder(self,parent,child):
        if parent == child and self._rootedge:
            raise NotBiconnected    # two roots, not even connected
        elif not self._rootedge and parent != child:
            self._rootedge = (parent,child)
        self._low[child] = self._dfsnumber[child] = len(self._dfsnumber)

    def backedge(self,source,destination):
        self._low[source] = min(self._low[source],self._dfsnumber[destination])

    def postorder(self,parent,child):
        if self._low[child] != self._dfsnumber[parent]:
            self._low[parent] = min(self._low[parent],self._low[child])
        elif (parent,child) == self._rootedge:
            pass                    # end of first component, >1 vertices
        elif parent != child:
            raise NotBiconnected    # articulation point
        elif not self._rootedge:
            self._rootedge = parent,child   # end of first component, isolani


def isBiconnected(G):
    """Return True if graph G is biconnected, False otherwise."""
    try:
        BiconnectivityTester(G)
        return True
    except NotBiconnected:
        return False


class stOrienter(DFS.Searcher):
    """
    Subclass for st-orienting a biconnected graph.
    """

    def __init__(self,G):
        """Relate edges for st-orientation."""
        if not isUndirected(G):
            raise ValueError("stOrienter: input not undirected graph")

        # set up data structures for DFS
        self._dfsnumber = {}
        self._low = {}
        self._down = {} # down[v] = child we're currently exploring from v
        self._lowv = {} # lowv[n] = vertex with low number n
        
        # The main data structure!
        # a dictionary mapping edges to lists of edges
        # each of which should be oriented the same as the key.
        self.orient = {}
        self.roots = [] # edges with no predecessor

        # perform the Depth First Search
        DFS.Searcher.__init__(self,G)

        # clean up now-useless data structures
        del self._dfsnumber, self._low, self._down, self._lowv

    def __iter__(self):
        """Return iterator for sequence of biconnected components."""
        return iter(self._components)

    def preorder(self,parent,child):
        self._low[child] = self._dfsnumber[child] = len(self._dfsnumber)
        self._lowv[self._low[child]] = self._down[parent] = child

    def backedge(self,source,destination):
        if self._dfsnumber[destination] < self._dfsnumber[source]:
            self._low[source] = min(self._low[source],
                                    self._dfsnumber[destination])
            if source != self._down[destination]:
                self.addOrientation(destination,source,destination)

    def postorder(self,parent,child):
        if self._low[child] != self._dfsnumber[parent]:
            self._low[parent] = min(self._low[parent],self._low[child])
            self.addOrientation(child,parent,self._lowv[self._low[child]])
        elif parent != child:
            self.roots.append((parent,child))

    def addOrientation(self,source,dest,anchor):
        """Store orientation info for source->dest edge.
        It should be oriented the same as the edge from the anchor
        to the current child of the anchor."""
        child = self._down[anchor]
        L = self.orient.setdefault((anchor,child),[])
        L.append((source,dest))

def stOrientation(G):
    """Find an acyclic orientation of G, with one source and one sink."""
    stO = stOrienter(G)
    if len(stO.roots) != 1:
        raise NotBiconnected

    source,dest = stO.roots[0]
    G = {v:set() for v in G}
    orientable = []

    while True:
        G[source].add(dest)
        for u,v in stO.orient.get((source,dest),[]):
            orientable.append((u,v))
        for v,u in stO.orient.get((dest,source),[]):
            orientable.append((u,v))
        if not orientable:
            break
        source,dest = orientable.pop()
    
    return G

# If run as "python Biconnectivity.py", run tests on various small graphs
# and check that the correct results are obtained.

class BiconnectivityTest(unittest.TestCase):
    G1 = {
        0: [1,2,5],
        1: [0,5],
        2: [0,3,4],
        3: [2,4,5,6],
        4: [2,3,5,6],
        5: [0,1,3,4],
        6: [3,4],
    }
    G2 = {
        0: [2,5],
        1: [3,8],
        2: [0,3,5],
        3: [1,2,6,8],
        4: [7],
        5: [0,2],
        6: [3,8],
        7: [4],
        8: [1,3,6],
    }

    def testIsBiconnected(self):
        """G1 is biconnected but G2 is not."""
        self.assertEqual(isBiconnected(self.G1), True)
        self.assertEqual(isBiconnected(self.G2), False)

    def testBiconnectedComponents(self):
        """G2 has four biconnected components."""
        C = BiconnectedComponents(self.G2)
        CV = sorted(sorted(component.keys()) for component in C)
        self.assertEqual(CV,[[0,2,5],[1,3,6,8],[2,3],[4,7]])
    
    def testSTOrientation(self):
        STO = stOrientation(self.G1)
        L = list(TopologicalOrder(STO))
        indegree = dict([(v,0) for v in self.G1])
        for v in L:
            for w in STO[v]:
                indegree[w] += 1
        outdegree = dict([(v,len(STO[v])) for v in self.G1])
        self.assertEqual(len([v for v in self.G1 if indegree[v] == 0]), 1)
        self.assertEqual(len([v for v in self.G1 if outdegree[v] == 0]), 1)

if __name__ == "__main__":
    unittest.main()   

