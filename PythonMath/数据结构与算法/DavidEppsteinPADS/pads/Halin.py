"""Halin.py

Reduction-based algorithm for recognizing Halin and D3-reducible graphs

D. Eppstein, January 2015.
"""

import unittest
from Graphs import copyGraph, isUndirected


# ============================================================
#     Main reduction algorithm for D3 reducible graphs
# ============================================================

def isK4(G):
    """Is this graph K4?"""
    if len(G) != 4:
        return False
    for v in G:
        if v in G[v] or len(set(G[v])) != 3:
            return False
    return True

def D3reducible(G,triangleHooks=[],pathHooks=[],finalize=isK4):
    """Test if the graph G is D3-reducible.

    Whenever a reduction is found, the hook functions are
    called in turn on it, and should return True if the reduction
    should be allowed to continue or False otherwise.

    The arguments to a triangle hook are the graph, the three
    triangle vertices, their three neighbors, and the id that
    will be given to the new vertex formed by the collapsed
    triangle. The arguments to a path hook are the graph, the
    three path vertices and the apex.
    
    The finalize hook takes as input the irreducible graph
    after all reductions are complete, and produces as output
    the return value for the overall computation.
    By default the return value is a Boolean that is true
    whenever the irreducible graph is K4."""
    if not isUndirected(G):
        raise TypeError("Argument to D3reducible must be an undirected graph")
    G = copyGraph(G)        # We are going to change G, so make a copy of it
    C = {v for v in G if len(G[v]) == 3}  # Active vertices, init. all w/deg=3

    def otherNeighbor(u,v,w):
        """Other neighbor of v given known neighbors u,w"""
        return [x for x in G[v] if x != u and x != w][0]

    def triangle(u,v,w):
        """Try a D3a reduction."""
        # u, v, and w are known to form a triangle but we still need to
        # check whether they have distinct neighbors."""
        Nu = otherNeighbor(v,u,w)
        Nv = otherNeighbor(u,v,w)
        Nw = otherNeighbor(u,w,v)
        if Nu == Nv or Nv == Nw or Nu == Nw:
            return      # Need to have three distinct neighbors
        x = object()    # Cons up an id for the triangle

        # Run the hooks
        for hook in triangleHooks:
            if not hook(G,u,v,w,Nu,Nv,Nw,x):
                return False

        # Make the change!
        del G[u],G[v],G[w]
        G[Nu].remove(u)
        G[Nv].remove(v)
        G[Nw].remove(w)
        G[x] = {Nu,Nv,Nw}
        G[Nu].add(x)
        G[Nv].add(x)
        G[Nw].add(x)

        # Update the active vertices
        C.update(z for z in (x,Nu,Nv,Nw) if len(G[z]) == 3)
    
    def path(u,v,w):
        """Try a D3b reduction."""
        # u, v, and w are known to induce a path but we still need to
        # check whether they have a common neighbor as apex."""
        apexes = G[u] & G[v] & G[w]
        if len(apexes) != 1:
            return
        apex = apexes.pop()

        # Run the hooks
        for hook in pathHooks:
            if not hook(G,u,v,w,apex):
                return False
        
        # Make the change!
        del G[v]
        G[u].remove(v)
        G[w].remove(v)
        G[apex].remove(v)
        G[u].add(w)
        G[w].add(u)
        
        # Update the active vertices
        if len(G[apex]) == 3:
            C.add(apex)
        pass

    def reduce(u,v,w):
        """Try a reduction in which v is the middle vertex"""
        for x in (u,v,w):
            if x not in G or len(G[x]) != 3:
                return      # No longer in G or not all degree 3, no redux
        if w in G[u]:
            triangle(u,v,w)
        else:
            path(u,v,w)
    
    while C:
        v = C.pop()
        if v in G and len(G[v]) == 3:
            p,q,r = tuple(G[v])     # Decode set of neighbors
            reduce(p,v,q)
            reduce(p,v,r)
            reduce(q,v,r)

    # Now check whether we found K4
    return finalize(G)

def reconstructD3(G,initialize,triangle,path,recognizer=D3reducible):
    """Recursively reconstruct a D3-reducible graph G
    by inverting the reductions used to recognize it.
    
    The other four arguments are functions:

    - recognize is a routine for performing D3 reductions
      on a graph with triangle hooks, path hooks, and a finalizer
      (like D3reducible or isHalin).

    - initialize is called first, as the finalizer from
      the recognition algorithm. Therefore, its signature
      should match what the recognizer is expecting.
      If any state passed in by the recognition phase is
      needed for later calls, it should be saved here,
      because it won't be passed in later. If the graph
      is not recognized, this should throw an exception.
    
    - triangle and path take the same eight and five arguments
      (respectively) as the triangle and path hooks from the
      reductions, but are called in the opposite order to
      the order they are called in the reductions."""
    
    calls = []

    def thook(*args):
        calls.append((triangle,args))
        return True

    def phook(*args):
        calls.append((path,args))
        return True

    recognizer(G,[thook],[phook],initialize)
    calls.reverse()
    for fun,args in calls:
        fun(*args)


# ============================================================
#     Additional reduction rules for Halin graphs
# ============================================================

def isOuterK4(G,outer):
    """Have we reduced to a K4 with a non-outer vertex?"""
    if not isK4(G):
        return False
    for v in G:
        if v not in outer:
            return True
    return False

def isHalin(G,triangleHooks=[],pathHooks=[],finalize=isOuterK4):
    """Test if the graph G is Halin.
    The two hook arguments are the same as for D3reducible,
    but the finalize argument takes two parameters:
    the final graph (as for D3reducible) and a set of
    vertices that have been marked as outer."""
    outer = set()           # Vertices that must be on the outer face
    
    def triangle(G,u,v,w,Nu,Nv,Nw,x):
        """Check and recolor vertices for triangle reduction"""
        if u in outer and v in outer and w in outer:
            return False    # Can't collapse when all three are outer
        outer.update(q for p,q in ((u,Nu),(v,Nv),(w,Nw)) if p in outer)
                            # Mark neighbors of outer as outer
        outer.add(x)        # As well as the new supervertex
        return True

    def path(G,u,v,w,x):
        """Check and recolor vertices for path reduction"""
        if x in outer:
            return False    # Can't shorten path with outer apex
        if len(G) == 5:
            outer.update(v for v in G if v != x)
        else:
            outer.update((u,w)) # Mark remaining path vertices as outer
        return True

    def final(H):
        """Have we reduced to a K4 with only one outer face?"""
        return finalize(H,outer)

    return D3reducible(G,[triangle]+triangleHooks,
                       [path]+pathHooks,final)

def HalinLeafVertices(G):
    """Reconstruct the leaf cycle of Halin graph G.
    The cycle is returned as a set of its vertices."""
    
    outer = set()
    def initialize(H,marked):
        """Augment outer to include all outer vertices"""
        if not isOuterK4(H,marked):
            raise TypeError("Argument to HalinLeafVertices must be Halin")
        for v in H:
            if v not in marked:
                outer.update(w for w in H if v != w)  # outerize all but v
                break

    def triangle(G,u,v,w,Nu,Nv,Nw,x):
        """Undo a D3a reduction"""
        nout = 0
        for (p,q) in ((u,Nu),(v,Nv),(w,Nw)):
            if q in outer:
                outer.add(p)
                nout += 1
        assert nout == 2

    def path(G,u,v,w,x):
        """Undo a D3b reduction"""
        assert x not in outer
        outer.update((u,v,w))

    reconstructD3(G,initialize,triangle,path,isHalin)
    return outer & set(iter(G))     # Find all marked vertices



# ============================================================
#     Hamiltonian cycle
# ============================================================

def D3HamiltonianCycle(G):
    ham = {}                # Where to put the Hamiltonian cycle

    def initialize(H):
        """Start a Hamiltonian cycle on a K4"""
        if not isK4(H):
            raise TypeError("Argument to D3HamiltonianCycle not D3 reducible")
        C = list(H)
        for i in range(4):
            ham[C[i-1]] = {C[i-2],C[i]}

    def triangle(G,u,v,w,Nu,Nv,Nw,x):
        """Undo D3a reduction on Hamiltonian cycle"""
        # Permute so the missing edge in the Hamiltonian cycle is Nw-x
        if Nu not in ham[x]:
            u,Nu,w,Nw = w,Nw,u,Nu
        elif Nv not in ham[x]:
            v,Nv,w,Nw = w,Nw,v,Nv
        assert w not in ham[x]

        # Out with the old, in with the new
        del ham[x]
        ham[Nu].remove(x)
        ham[Nu].add(u)
        ham[Nv].remove(x)
        ham[Nv].add(v)
        ham[u] = {Nu,w}
        ham[w] = {u,v}
        ham[v] = {w,Nv}

    def path(G,u,v,w,x):
        """Undo D3b reduction on Hamiltonian cycle"""
        if w not in ham[u]: w = x    # Permute so w is a ham-neighbor of u
        ham[u].remove(w)
        ham[u].add(v)
        ham[w].remove(u)
        ham[w].add(v)
        ham[v] = {u,w}

    reconstructD3(G,initialize,triangle,path)
    return ham


# ============================================================
#     Additional reduction rules for other graph classes
# ============================================================

def isDual3Tree(G,triangleHooks=[],pathHooks=[],finalize=isK4):
    """Test if the graph G is the dual of a 3-tree."""
    def noPath(G,u,v,w,x): return False
    return D3reducible(G,triangleHooks,[noPath],finalize)

def isWheel(G,triangleHooks=[],pathHooks=[],finalize=isK4):
    """Test if the graph G is a wheel."""
    def noTriangle(G,u,v,w,Nu,Nv,Nw,x): return False
    return D3reducible(G,[noTriangle],pathHooks,finalize)


# ============================================================
#     If run from command line, perform unit tests
# ============================================================

class HalinTest(unittest.TestCase):
    cube = {i:[i^1,i^2,i^4] for i in range(8)}
    trunctet = {(i,j):[(i,k) for k in range(4) if k!=i and k!=j]+[(j,i)]
                for i in range(4) for j in range(4) if i!=j}
    wheel = {0:[1,2,3,4,5],1:[0,2,5],2:[0,1,3],3:[0,2,4],4:[0,3,5],5:[0,1,4]}
    halin8 = {0:[1,7,5],1:[0,2,7],2:[1,3,6],3:[2,4,6],
              4:[3,5,6],5:[0,4,6],6:[2,3,4,5,7],7:[0,1,6]}
    nonhalin = {0:[1,2,4],1:[0,3,5,7],2:[0,3,4,6],3:[1,2,7],
                4:[0,2,6],5:[1,6,7],6:[2,4,5],7:[1,3,5]}
    ternary = {0:(1,2,3),13:(4,14,39),39:(12,13,38)}
    for i in range(1,13):
        ternary[i] = ((i-1)//3,3*i+1,3*i+2,3*i+3)
    for i in range(14,39):
        ternary[i] = ((i-1)//3,i-1,i+1)

    def testD3Reducible(self):
        """Check correct classification of D3-reducible graphs"""
        self.assertEqual(D3reducible(self.cube), False)
        self.assertEqual(D3reducible(self.trunctet), True)
        self.assertEqual(D3reducible(self.wheel), True)
        self.assertEqual(D3reducible(self.nonhalin), True)
        self.assertEqual(D3reducible(self.ternary), True)

    def testReductionTypes(self):
        """Check that the correct reduction types are being applied"""
        self.assertEqual(isWheel(self.trunctet),False)
        self.assertEqual(isWheel(self.wheel),True)
        self.assertEqual(isWheel(self.ternary),False)
        self.assertEqual(isWheel(self.nonhalin), False)
        self.assertEqual(isDual3Tree(self.trunctet),True)
        self.assertEqual(isDual3Tree(self.wheel),False)
        self.assertEqual(isDual3Tree(self.ternary),False)
        self.assertEqual(isDual3Tree(self.nonhalin), False)

    def testHalin(self):
        """Check correct classification of Halin graphs"""
        self.assertEqual(isHalin(self.cube), False)
        self.assertEqual(isHalin(self.trunctet), False)
        self.assertEqual(isHalin(self.wheel), True)
        self.assertEqual(isHalin(self.halin8), True)
        self.assertEqual(isHalin(self.nonhalin), False)
        self.assertEqual(isHalin(self.ternary), True)
        self.assertEqual(HalinLeafVertices(self.wheel),{1,2,3,4,5})
        self.assertEqual(HalinLeafVertices(self.halin8),{0,1,2,3,4,5})
        self.assertEqual(HalinLeafVertices(self.ternary),set(range(13,40)))

    def testHamiltonian(self):
        """Check correct construction of Hamiltonian cycle"""
        for G in (self.trunctet,self.wheel,self.nonhalin,self.ternary):
            H = D3HamiltonianCycle(G)
            self.assertEqual(set(H),set(G))     # same vertices?
            for v in H:
                self.assertEqual(len(H[v]),2)   # degree-two?
                for w in H[v]:
                    self.assertEqual(w in G[v], True)   # subgraph?

if __name__ == "__main__":
    unittest.main()  
