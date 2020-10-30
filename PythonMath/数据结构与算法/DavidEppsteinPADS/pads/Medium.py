"""Medium.py

Algorithms for media; see e.g. my paper arxiv:cs.DS/0206033.
As a very brief introduction to media theory:

- A medium consists of a set of states, a set of tokens,
  and an "action" that produces a new state St from a state S and a token t.
  An action is "effective" if St != S.
- Each token t has a "reverse" r such that St = V != S iff Vr = S != V.
- Any two states can be connected by a sequence of actions that
  uses each token at most once and does not use both a token and its reverse.
- In any sequence of effective actions taking a state back to itself, 
  the tokens can be matched up in token-reverse pairs.

The resulting theory is equivalent to that for partial cubes (graphs that
can be embedded in a distance-preserving way into hypercubes): the state-
transition graphs of media are partial cubes, and any partial cube
corresponds to a medium in this way. However, media theory provides a
different perspective on these structures that more closely resembles the
theory of finite automata.

D. Eppstein, May 2007.
"""
    
import BFS,DFS
from Graphs import isUndirected
import unittest

class MediumError(ValueError): pass

class Medium:
    """
    Base class for media.
    
    A medium is defined by four instance methods:
    - M.states() lists the states of M
    - M.tokens() lists the tokens of M
    - M.reverse(token) finds the token with opposite action to its argument
    - M.action(state,token) gives the result of applying that token
    These should be defined in subclasses; the base does not define them.
    
    In addition, we define methods (that may possibly be overridden):
    - iter(M) is a synonym for M.states()
    - len(M) is a synonym for len(M.states())
    - M.effective(state) lists tokens effective on that state
    - M[state] returns a dict mapping tokens to actions
    - M(state,token) is a synonym for M.action(state,token)
    """

    def __iter__(self):
        """Generate sequence of medium states."""
        return self.states()
    
    def __len__(self):
        """Return number of states in the medium."""
        i = 0
        for S in self.states():
            i += 1
        return i

    def __getitem__(self,S):
        """Construct dict mapping tokens to actions from state S."""
        return {t:self.action(S,t) for t in self.tokens()}

    def __call__(self,S,t):
        """Apply token t to state S."""
        return self.action(S,t)


class ExplicitMedium(Medium):
    """
    Medium in which all dicts M[state] have been precomputed.
    This can be less space-efficient than other representations
    (since it essentially involves a big table with size
    (# states) x (# tokens) but it makes all operations fast.
    """

    def __init__(self,M):
        """Form ExplicitMedium from any other kind of medium."""
        self._reverse = {t:M.reverse(t) for t in M.tokens()}
        self._action = {S:M[S] for S in M}

    # Basic classes needed to define any medium

    def states(self):
        return iter(self._action)

    def tokens(self):
        return iter(self._reverse)

    def reverse(self,t):
        return self._reverse[t]

    def action(self,S,t):
        return self._action[S][t]

    # Faster implementation of other medium functions

    def __len__(self):
        return len(self._action)

    def __getitem__(self,S):
        return self._action[S]


class BitvectorMedium(Medium):
    """
    Medium defined by a set of bitvectors.
    
    The tokens of the medium are pairs (i,b) where i is an index
    into a bitvector and b is a bit; the action of a token on a bitvector
    is to change the i'th bit to b, if the result is part of the set,
    and if not to leave the bitvector unchanged.
    
    We assume but do not verify that the bitvectors do form a medium;
    that is, that one can transform any bitvector in the set into any
    other via a sequence of actions of length equal to the Hamming
    distance between the vectors.
    """

    def __init__(self,states,L):
        """Initialize medium for set states and bitvector length L."""
        self._states = set(states)
        self._veclen = L
    
    def states(self):
        return iter(self._states)

    def tokens(self):
        for i in range(self._veclen):
            yield i,False
            yield i,True

    def reverse(self,t):
        i,b = t
        return i,not b

    def action(self,S,t):
        """
        Compute the action of token t on state S.
        We form the bitvector V that should correspond to St,
        then test whether V belongs to the given set of states.
        If so, we return it; otherwise, we return S itself.
        """
        i,b = t
        mask = 1<<i
        if b:
            V = S | mask
        else:
            V = S &~ mask
        if V in self._states:
            return V
        else:
            return S


def StateTransitionGraph(M):
    """
    Build a graph G describing the states and transitions of medium M.
    If s is a state of M, G[s] will provide a dictionary mapping
    the neighbors of s to the actions that produced those neighbors.
    """
    G = {S:{} for S in M}
    for S in M:
        for t in M.tokens():
            St = M(S,t)
            if St != S:
                if St in G[S]:
                    raise MediumError("multiple adjacency from %s to %s" % (S,St))
                G[S][St] = t
    return G


class LabeledGraphMedium(Medium):
    """
    A medium defined from an edge-labeled graph.
    The input graph G should have the property that G[v][w] is a token
    that transforms v to w. For instance,
    LabeledGraphMedium(StateTransitionGraph(M)) should result
    in a medium with the same behavior as M itself.
    """
    def __init__(self,G):
        if not isUndirected(G):
            raise MediumError("not an undirected graph")
        self._action = {v:{} for v in G}
        self._reverse = {}
        for v in G:
            for w in G[v]:
                t = G[v][w]
                if t in self._action[v]:
                    raise MediumError("multiple edges for state %s and token %s" % (v,t))
                self._action[v][t] = w
                if t not in self._reverse:
                    rt = G[w][v]
                    if rt in self._reverse:
                        raise MediumError("mismatched token reversals")
                    self._reverse[t] = rt
                    self._reverse[rt] = t
                elif G[w][v] != self._reverse[t]:
                    raise MediumError("mismatched token reversals")

    def states(self):
        return iter(self._action)

    def tokens(self):
        return iter(self._reverse)

    def reverse(self,t):
        return self._reverse[t]

    def action(self,S,t):
        return self._action[S].get(t,S)
    
    def __len__(self):
        return len(self._action)


def RoutingTable(M):
    """
    Return a dictionary mapping pairs (state1,state2) to tokens,
    such that the action of the token takes state1 closer to state2.
    By following successive tokens from this table, we can find
    a path in the medium that uses each token at most once
    and involves no token-reverse pairs.
    
    We use the O(n^2) time algorithm from arxiv:cs.DS/0206033.
    This is also a key step of the partial cube recognition algorithm
    from arxiv:0705.1025 -- as part of that algorithm, if we
    recognize that the input is not a medium, we raise MediumError.
    """
    G = StateTransitionGraph(M)
    current = initialState = next(iter(M))

    # find list of tokens that lead to the initial state
    activeTokens = set()
    for LG in BFS.BreadthFirstLevels(G,initialState):
        for v in LG:
            for w in LG[v]:
                activeTokens.add(G[w][v])
    for t in activeTokens:
        if M.reverse(t) in activeTokens:
            raise MediumError("shortest path to initial state is not concise")
    activeTokens = list(activeTokens)
    inactivated = object()  # flag object to mark inactive tokens

    # rest of data structure: point from states to list and list to states
    activeForState = {S:-1 for S in M}
    statesForPos = [[] for i in activeTokens]
    
    def scan(S):
        """Find the next token that is effective for s."""
        i = activeForState[S]
        while True:
            i += 1
            if i >= len(activeTokens):
                raise MediumError("no active token from %s to %s" %(S,current))
            if activeTokens[i] != inactivated and M(S,activeTokens[i]) != S:
                activeForState[S] = i
                statesForPos[i].append(S)
                return
    
    # set initial active states
    for S in M:
        if S != current:
            scan(S)

    # traverse the graph, maintaining active tokens
    visited = set()
    routes = {}
    for prev,current,edgetype in DFS.search(G,initialState):
        if prev != current and edgetype != DFS.nontree:
            if edgetype == DFS.reverse:
                prev,current = current,prev
            
            # add token to end of list, point to it from old state
            activeTokens.append(G[prev][current])
            activeForState[prev] = len(activeTokens) - 1
            statesForPos.append([prev])
            
            # inactivate reverse token, find new token for its states
            activeTokens[activeForState[current]] = inactivated
            for S in statesForPos[activeForState[current]]:
                if S != current:
                    scan(S)

            # remember routing table as part of returned results
            if current not in visited:
                for S in M:
                    if S != current:
                        routes[S,current] = activeTokens[activeForState[S]]

    return routes


def HypercubeEmbedding(M):
    """Map medium states isometrically onto a hypercube."""
    dim = 0
    tokmap = {}
    for t in M.tokens():
        if t not in tokmap:
            tokmap[t] = tokmap[M.reverse(t)] = 1<<dim
            dim += 1
    embed = {}
    G = StateTransitionGraph(M)
    for prev,current,edgetype in DFS.search(G):
        if edgetype == DFS.forward:
            if prev == current:
                embed[current] = 0
            else:
                embed[current] = embed[prev] ^ tokmap[G[prev][current]]
    return embed


# Perform some sanity checks if run standalone

class MediumTest(unittest.TestCase):

    # make medium from all five-bit numbers that have 2 or 3 bits lit
    twobits = [3,5,6,9,10,12,17,18,20,24]
    threebits = [31^x for x in twobits]
    M523 = BitvectorMedium(twobits+threebits,5)

    def testStates(self):
        """Check that iter(Medium) generates the correct set of states."""
        M = MediumTest.M523
        L1 = list(M)
        L1.sort()
        L2 = MediumTest.twobits + MediumTest.threebits
        L2.sort()
        self.assertEqual(L1,L2)
    
    def testTokens(self):
        """Check that Medium.tokens() generates the correct set of tokens."""
        M = MediumTest.M523
        toks = [(i,False) for i in range(5)] + [(i,True) for i in range(5)]
        self.assertEqual(set(toks),set(M.tokens()))
        for t in toks:
            i,b = t
            self.assertEqual(M.reverse(t),(i,not b))
    
    def testAction(self):
        """Check that the action of the tokens is what we expect."""
        M = MediumTest.M523
        for x in M:
            for i in range(5):
                b = (x>>i)&1
                self.assertEqual(x,M(x,(i,b)))
                y = M(x,(i,not b))
                if b == (x in MediumTest.twobits):
                    self.assertEqual(x,y)
                else:
                    self.assertEqual(y,x^(1<<i))
    
    def testRouting(self): 
        """Check that RoutingTable finds paths that decrease Hamming dist."""
        M = MediumTest.M523
        R = RoutingTable(M)
        for x in M:
            for y in M:
                if x != y:
                    i,b = R[x,y]
                    self.assertEqual((x^y)&(1<<i),1<<i)
                    self.assertEqual((x>>i)&1, not b)
    
    def testExplicit(self):            
        """Check that ExplicitMedium looks the same as its argument."""
        M = MediumTest.M523
        E = ExplicitMedium(M)
        self.assertEqual(set(M),set(E))
        self.assertEqual(set(M.tokens()),set(E.tokens()))
        for t in M.tokens():
            self.assertEqual(M.reverse(t),E.reverse(t))
        for s in M:
            for t in M.tokens():
                self.assertEqual(M(s,t),E(s,t))

    def testEmbed(self):
        """Check that HypercubeEmbedding finds appropriate coordinates."""
        M = MediumTest.M523
        E = HypercubeEmbedding(M)
        def ham(x,y):
            z = x^y
            d = 0
            while z:
                d += 1
                z &= z-1
            return d
        for x in M:
            for y in M:
                self.assertEqual(ham(x,y),ham(E[x],E[y]))     

    def testGraph(self):
        """Check that LabeledGraphMedium(StateTransitionGraph(M)) = M."""
        M = MediumTest.M523
        L = LabeledGraphMedium(StateTransitionGraph(M))
        self.assertEqual(set(M),set(L))
        self.assertEqual(set(M.tokens()),set(L.tokens()))
        for t in M.tokens():
            self.assertEqual(M.reverse(t),L.reverse(t))
        for s in M:
            for t in M.tokens():
                self.assertEqual(M(s,t),L(s,t))

if __name__ == "__main__":
    unittest.main()

