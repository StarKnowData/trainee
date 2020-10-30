"""PartialCube.py

Test whether a graph is an isometric subgraph of a hypercube.

D. Eppstein, September 2005, rewritten May 2007 per arxiv:0705.1025.
"""

import BFS
import Medium
from Bipartite import isBipartite
from UnionFind import UnionFind
from StrongConnectivity import StronglyConnectedComponents
from Graphs import isUndirected
import unittest

def PartialCubeEdgeLabeling(G):
    """
    Label edges of G by their equivalence classes in a partial cube structure.

    We follow the algorithm of arxiv:0705.1025, in which a number of
    equivalence classes equal to the maximum degree of G can be found
    simultaneously by a single breadth first search, using bitvectors.
    However, in order to avoid deep recursions (problematic in Python)
    we use a union-find data structure to keep track of edge identifications
    discovered so far. That is, we repeatedly contract our initial graph,
    maintaining as we do the property that G[v][w] points to a union-find
    set representing edges in the original graph that have been contracted
    to the single edge v-w.
    """
    
    # Some simple sanity checks
    if not isUndirected(G):
        raise Medium.MediumError("graph is not undirected")
    L = list(StronglyConnectedComponents(G))
    if len(L) != 1:
        raise Medium.MediumError("graph is not connected")

    # Set up data structures for algorithm:
    # - UF: union find data structure representing known edge equivalences
    # - CG: contracted graph at current stage of algorithm
    # - LL: limit on number of remaining available labels
    UF = UnionFind()
    CG = {v:{w:(v,w) for w in G[v]} for v in G}
    NL = len(CG)-1
    
    # Initial sanity check: are there few enough edges?
    # Needed so that we don't try to use union-find on a dense
    # graph and incur superquadratic runtimes.
    n = len(CG)
    m = sum([len(CG[v]) for v in CG])
    if 1<<(m//n) > n:
        raise Medium.MediumError("graph has too many edges")

    # Main contraction loop in place of the original algorithm's recursion
    while len(CG) > 1:    
        if not isBipartite(CG):
            raise Medium.MediumError("graph is not bipartite")

        # Find max degree vertex in G, and update label limit
        deg,root = max([(len(CG[v]),v) for v in CG])
        if deg > NL:
            raise Medium.MediumError("graph has too many equivalence classes")
        NL -= deg

        # Set up bitvectors on vertices
        bitvec = {v:0 for v in CG}
        neighbors = {}
        i = 0
        for neighbor in CG[root]:
            bitvec[neighbor] = 1<<i
            neighbors[1<<i] = neighbor
            i += 1

        # Breadth first search to propagate bitvectors to the rest of the graph
        for LG in BFS.BreadthFirstLevels(CG,root):
            for v in LG:
                for w in LG[v]:
                    bitvec[w] |= bitvec[v]

        # Make graph of labeled edges and union them together
        labeled = {v:set() for v in CG}
        for v in CG:
            for w in CG[v]:
                diff = bitvec[v]^bitvec[w]
                if not diff or bitvec[w] &~ bitvec[v] == 0:
                    continue    # zero edge or wrong direction
                if diff not in neighbors:
                    raise Medium.MediumError("multiply-labeled edge")
                neighbor = neighbors[diff]
                UF.union(CG[v][w],CG[root][neighbor])
                UF.union(CG[w][v],CG[neighbor][root])
                labeled[v].add(w)
                labeled[w].add(v)

        # Map vertices to components of labeled-edge graph
        component = {}
        compnum = 0
        for SCC in StronglyConnectedComponents(labeled):
            for v in SCC:
                component[v] = compnum
            compnum += 1

        # generate new compressed subgraph
        NG = {i:{} for i in range(compnum)}
        for v in CG:
            for w in CG[v]:
                if bitvec[v] == bitvec[w]:
                    vi = component[v]
                    wi = component[w]
                    if vi == wi:
                        raise Medium.MediumError("self-loop in contracted graph")
                    if wi in NG[vi]:
                        UF.union(NG[vi][wi],CG[v][w])
                    else:
                        NG[vi][wi] = CG[v][w]
        
        CG = NG

    # Here with all edge equivalence classes represented by UF.
    # Turn them into a labeled graph and return it.
    return {v:{w:UF[v,w] for w in G[v]} for v in G}


def MediumForPartialCube(G):
    """
    Find a medium corresponding to the partial cube G.
    Raises MediumError if G is not a partial cube.
    Uses the O(n^2) time algorithm of arxiv:0705.1025.
    """
    L = PartialCubeEdgeLabeling(G)
    M = Medium.LabeledGraphMedium(L)
    Medium.RoutingTable(M)   # verification step per arxiv:0705.1025
    return M


def PartialCubeLabeling(G):
    """Return vertex labels with Hamming distance = graph distance."""
    return Medium.HypercubeEmbedding(MediumForPartialCube(G))


def isPartialCube(G):
    """Test whether the given graph is a partial cube."""
    try:
        MediumForPartialCube(G)
        return True
    except Medium.MediumError:
        return False



# Perform some sanity checks if run standalone

class PartialCubeTest(unittest.TestCase):

    # make medium from all five-bit numbers that have 2 or 3 bits lit
    twobits = [3,5,6,9,10,12,17,18,20,24]
    threebits = [31^x for x in twobits]
    M523 = Medium.BitvectorMedium(twobits+threebits,5)

    def testIsPartialCube(self):
        M = PartialCubeTest.M523
        G = Medium.StateTransitionGraph(M)
        I = isPartialCube(G)
        self.assertEqual(I,True)
    
    def testK4(self):
        G = {i:[j for j in range(4) if j != i] for i in range(4)}
        self.assertEqual(isPartialCube(G),False)

    def testK33(self):
        G = {0:[3,4,5],1:[3,4,5],2:[3,4,5],3:[0,1,2],4:[0,1,2],5:[0,1,2]}
        self.assertEqual(isPartialCube(G),False)

    def testMediumForPartialCube(self):
        """Check that we get an isomorphic medium via MediumForPartialCube."""
        # Note that we do not get the same tokens.
        # So, we need to check equality of graphs
        # rather than equality of media.
        M = PartialCubeTest.M523
        G = Medium.StateTransitionGraph(M)
        E = MediumForPartialCube(G)
        H = Medium.StateTransitionGraph(E)
        self.assertEqual(set(G),set(H))
        for v in G:
            self.assertEqual(set(G[v]),set(H[v]))

    def test6212(self):
        """
        A graph that can be labeled, but is not a partial cube.
        Tests the code in LabeledGraphMedium that checks for the
        existence of multiple equally labeled edges at a vertex.
        """
        n,a,b,c = 6,2,1,2
        G = {}
        for i in range(n):
            G[i,0] = [(i,1),((i+b)%n,3),((i+c)%n,3)]
            G[i,1] = [(i,0),(i,2),((i-a)%n,2)]
            G[i,2] = [(i,1),(i,3),((i+a)%n,1)]
            G[i,3] = [(i,2),((i-b)%n,0),((i-c)%n,0)]
        self.assertEqual(isPartialCube(G),False)

    def test61150(self):
        """
        Another graph that can be labeled, but is not a partial cube.
        Tests the code in RoutingTable that makes sure that only tokens
        in a single direction belong to the initial list of active tokens.
        """
        G = {}
        n,a,b,c,d = 6,1,1,5,0
        for i in range(n):
            G[i,0] = [(i,1),((i+a)%n,5),((i+b)%n,3)]
            G[i,1] = [(i,0),(i,2),((i-d)%n,4)]
            G[i,2] = [(i,1),(i,3),((i+c)%n,5)]
            G[i,3] = [(i,2),(i,4),((i-b)%n,0)]
            G[i,4] = [(i,3),(i,5),((i+d)%n,1)]
            G[i,5] = [(i,4),((i-a)%n,0),((i-c)%n,2)]
        self.assertEqual(isPartialCube(G),False)

if __name__ == "__main__":
    unittest.main()
