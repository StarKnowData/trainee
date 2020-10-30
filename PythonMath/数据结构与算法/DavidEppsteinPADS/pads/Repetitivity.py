"""Repetitivity.py

Repetitivity analysis in graphs: algorithms for taking as input an
edge-labeled graph and finding paths or cycles in which no two
consecutive edges have the same label.

D. Eppstein, July 2005.
"""

from StrongConnectivity import StronglyConnectedComponents
import DFS

class NonrepetitiveGraph:
    """
    Data structure for finding nonrepetitive paths in graphs.
    If G is a digraph, with G[v][w] = a collection of labels
    of the edge from v to w, then NonrepetitiveGraph(G) allows
    us to find paths in G, with a choice of label per edge of
    the path, such that no two consecutive labels are equal.
    
    If NR is a NonrepetitiveGraph instance, then
    - iter(NR) lists the vertices in NR
    - NR[v] lists the labels incident to vertex v
    - cyclic() generates a sequence of triples (v,w,label)
      that can be part of nonrepetitive cycles in NR
    - reachable(v,label) generates a sequence of pairs
      (w,label) that can be reached by nonrepetitive
      paths starting from v with the given label.
    - shortest(v,label,w,label) finds a shortest path between
      the given vertex,label pairs.
    """
    
    def __init__(self,G):
        """
        Initialize from a given graph instance.  The graph G
        should have G[v][w] equal to a collection (list, set, etc)
        of the labels on edges from v to w; this allows us to
        represent multigraphs with differing labels on their
        multiedges.
        
        Data stored in fields of this instance:
        - self.nrg is a transformed unlabeled graph in which paths
          represent nonrepetitive paths in G
        - self.labels is a dictionary mapping vertices to their
          label sets
        """
        self.labels = {}
        for v in G:
            self.labels[v] = set()
            for w in G[v]:
                self.labels[w] = set()
        for v in G:
            for w in G[v]:
                self.labels[v].update(G[v][w])
                self.labels[w].update(G[v][w])
        self.nrg = {}
        for v in self:
            self._gadget(v,self.labels[v])
        for v in G:
            for w in G[v]:
                for L in G[v][w]:
                    self.nrg[v,L,False].add((w,L,True))
    
    def __getitem__(self,v):
        """x.__getitem__(y) <==> x[y]"""
        return self.labels[v]

    def __contains__(self,v):
        """x.__contains__(y) <==> y in x"""
        return v in self.labels

    def __iter__(self):
        """x.__iter__() <==> iter(x)"""
        return iter(self.labels)

    def _gadget(self,v,labels):
        """Create nonrepetitivity gadget for vertex v and given label set."""
        labels = list(labels)
        for L in labels:
            self.nrg.setdefault((v,L,True),set())
            self.nrg.setdefault((v,L,False),set())
        if len(labels) == 1:
            return
        groups = []
        n = len(labels)
        while n > 0:
            if n % 3 == 0:
                grouplen = 3
            else:
                grouplen = 2
            group = labels[n-grouplen:n]
            for L1 in group:
                for L2 in group:
                    if L1 != L2:
                        self.nrg[v,L1,True].add((v,L2,False))
            if len(labels) > 3:
                groups.append(object())
                self.nrg[v,groups[-1],False] = {(v,L,False) for L in group}
                for L in group:
                    self.nrg[v,L,True].add((v,groups[-1],True))
            n -= grouplen
        if len(groups) > 1:
            self._gadget(v,groups)

    def cyclic(self):
        """Yield triples (v,w,label) belonging to all nonrepetitive cycles."""
        components = {}
        for C in StronglyConnectedComponents(self.nrg):
            for v in C:
                components[v] = C
        for v in self:
            for L in self[v]:
                for w,LL,bit in self.nrg[v,L,False]:
                    if components[v,L,False] == components[w,L,True]:
                        yield v,w,L

    def reachable(self,v,L):
        """Yield pairs (w,label) on nonrepetitive paths from v,L."""
        if v not in self or L not in self[v]:
            return
        for w,LL,bit in DFS.preorder(self.nrg,(v,L,False)):
            if bit and LL in self[w]:
                yield w,LL

    def _flattenpath(self,path):
        """Helper routine for shortest: convert output from internal format."""
        output = []
        while path:
            output.append(path[0])
            path = path[1]
        output.reverse()
        return output

    def shortest(self,v,L,w,LL):
        """
        Breadth first search for shortest path from (v,L) to (w,LL).
        The path is returned as a list of vertices.
        """
        start = (v,L,False)
        visited = {start}
        thislevel = [(start,(v,None))]
        nextlevel = []
        levelindex = 0
        while levelindex < len(thislevel) or nextlevel:
            if levelindex >= len(thislevel):
                thislevel = nextlevel
                nextlevel = []
                levelindex = 0
            current,path = thislevel[levelindex]
            levelindex += 1
            for nrgnode in self.nrg[current]:
                if nrgnode not in visited:
                    if nrgnode[2] and not current[2]:   # non-gadget edge?
                        newpath = (nrgnode[0],path)
                        if nrgnode[:2] == (w,LL):
                            return self._flattenpath(newpath)
                        nextlevel.append((nrgnode,newpath))
                    else:
                        thislevel.append((nrgnode,path))
                    visited.add(nrgnode)
        raise ValueError("No such path exists")