"""BipartiteMatching.py

Hopcroft-Karp bipartite maximum-cardinality matching and maximum
independent set for bipartite graphs.

D. Eppstein, April 2002.
"""

from StrongConnectivity import StronglyConnectedComponents

def matching(graph):
    """
    Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to lists
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.
    """

    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break

    while True:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = {u:unmatched for u in graph}
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)

        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)

        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return True
            return False

        for v in unmatched: recurse(v)

def imperfections(graph):
    """
    Find edges that do not belong to any perfect matching of G.
    The input format is the same as for matching(), and the output
    is a subgraph of the input graph in the same format.
    
    For each edge v->w in the output subgraph, imperfections[v][w]
    is itself a subgraph of the input, induced by a set of
    vertices that must be matched to each other, including w but
    not including v.
    """
    M,A,B = matching(graph)
    if len(M) != len(graph):
        return graph    # whole graph is imperfect

    orientation = {}
    for v in graph:
        orientation[v,True]=[]
        for w in graph[v]:
            if M[w] == v:
                orientation[w,False]=[(v,True)]
            else:
                orientation[v,True].append((w,False))

    components = {}
    for C in StronglyConnectedComponents(orientation):
        induced = {v:{w for w,bit2 in C[v,bit]} for v,bit in C if bit}
        for v,bit in C:
            if not bit:   # don't forget the matched edges!
                induced.setdefault(M[v],set()).add(v)
        for v in C:
            components[v] = induced

    imperfections = {}
    for v in graph:
        imperfections[v] = {w:components[w,False] for w in graph[v]
                                 if M[w] != v and
                                 components[v,True] != components[w,False]}
    
    return imperfections
