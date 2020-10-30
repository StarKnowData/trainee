"""StrongConnectivity.py

DFS-based algorithm for computing strongly connected components.

If G is a graph, then
- StronglyConnectedComponents(G) returns a list of
  its components, each represented as a subgraph of G
- Condensation(G) returns a directed acyclic graph, the
  vertices of which are strongly connected components of G.
  Each vertex of the condensation is represented as a frozenset
  of the vertices of G within a single strongly connected component.

D. Eppstein, July 2005.
"""

import unittest
import DFS

class StronglyConnectedComponents(DFS.Searcher):
    """
    Generate the strongly connected components of G.  G should be
    represented in such a way that "for v in G" loops through the
    vertices, and "G[v]" produces a list of the neighbors of v;
    for instance, G may be a dictionary mapping each vertex to its
    neighbor set.  The result of StronglyConnectedComponents(G) is
    a sequence of subgraphs of G.
    """

    def __init__(self,G):
        """Search for strongly connected components of graph G."""

        # set up data structures for DFS
        self._components = []
        self._dfsnumber = {}
        self._activelen = {}
        self._active = []
        self._low = {}
        self._biglow = len(G)
        self._graph = G

        # perform the Depth First Search
        DFS.Searcher.__init__(self,G)

        # clean up now-useless data structures
        del self._dfsnumber, self._activelen, self._active, self._low

    def __iter__(self):
        """Return iterator for sequence of strongly connected components."""
        return iter(self._components)

    def __len__(self):
        """How many components are there?"""
        return len(self._components)

    def _component(self,vertices):
        """Make a new SCC."""
        vertices = set(vertices)
        induced = {v:{w for w in self._graph[v] if w in vertices} for v in vertices}
        self._components.append(induced)

    def preorder(self,parent,child):
        """Handle first visit to vertex in DFS search for components."""
        if parent == child:
            self._active = []
        self._activelen[child] = len(self._active)
        self._active.append(child)
        self._low[child] = self._dfsnumber[child] = len(self._dfsnumber)

    def backedge(self,source,destination):
        """Handle non-tree edge in DFS search for components."""
        self._low[source] = min(self._low[source],self._low[destination])

    def postorder(self,parent,child):
        """Handle last visit to vertex in DFS search for components."""
        if self._low[child] == self._dfsnumber[child]:
            self._component(self._active[self._activelen[child]:])
            for v in self._components[-1]:
                self._low[v] = self._biglow
            del self._active[self._activelen[child]:]
        else:
            self._low[parent] = min(self._low[parent],self._low[child])

def Condensation(G):
    """Return a DAG with vertices equal to sets of vertices in SCCs of G."""
    components = {}
    GtoC = {}
    for C in StronglyConnectedComponents(G):
        C = frozenset(C)
        for v in C:
            GtoC[v] = C
        components[C] = set()
    for v in G:
        for w in G[v]:
            if GtoC[v] != GtoC[w]:
                components[GtoC[v]].add(GtoC[w])
    return components
    
# If run as "python StrongConnectivity.py", run tests on various small graphs
# and check that the correct results are obtained.

class StrongConnectivityTest(unittest.TestCase):

    G1 = { 0:[1], 1:[2,3], 2:[4,5], 3:[4,5], 4:[6], 5:[], 6:[] }
    C1 = [[0],[1],[2],[3],[4],[5],[6]]

    # Work around http://bugs.python.org/issue11796 by using a loop
    # instead of a dict/set comprehension in a class variable initializer
    # should be:
    # Con1 = {frozenset([v]):{frozenset([w]) for w in G1[v]} for v in G1}
    Con1 = {}
    for v in G1:
        Con1[frozenset([v])] = {frozenset([w]) for w in G1[v]}
    
    G2 = { 0:[1], 1:[2,3,4], 2:[0,3], 3:[4], 4:[3] }
    C2 = [[0,1,2],[3,4]]
    f012 = frozenset([0,1,2])
    f34 = frozenset([3,4])
    Con2 = {f012:{f34}, f34:set()}
    
    knownpairs = [(G1,C1),(G2,C2)]

    def testStronglyConnectedComponents(self):
        """Check known graph/component pairs."""
        for (graph,expectedoutput) in self.knownpairs:
            output = [list(C) for C in StronglyConnectedComponents(graph)]
            for component in output:
                component.sort()
            output.sort()
            self.assertEqual(output,expectedoutput)

    def testSubgraph(self):
        """Check that each SCC is an induced subgraph."""
        for (graph,expectedoutput) in self.knownpairs:
            components = StronglyConnectedComponents(graph)
            for C in components:
                for v in C:
                    for w in graph:
                        self.assertEqual(w in graph[v] and w in C, w in C[v])

    def testCondensation(self):
        """Check that the condensations are what we expect."""
        self.assertEqual(Condensation(self.G1),self.Con1)
        self.assertEqual(Condensation(self.G2),self.Con2)

if __name__ == "__main__":
    unittest.main()   

