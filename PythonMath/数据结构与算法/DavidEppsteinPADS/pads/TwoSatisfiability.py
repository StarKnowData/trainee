"""TwoSatisfiability.py

Algorithms for solving 2-satisfiability problems.
For theory and references, see http://en.wikipedia.org/wiki/2-satisfiability

All instances should be represented as a directed implication graph in which
the vertices represent variables and (via Not.py) their negations. A variable
may be represented by any hashable Python object, and its negation should
be represented by the object Not(x). For instance, the implication graph
    {1:[2,3], 2:[Not(1),3]}
from the unit tests of this module represents the system of implications
among three logical variables v1, v2, and v3:
    v1 => v2, v1 => v3;  v2 => ~v1, v2 => v3.
An instance is satisfiable if it is possible to assign the Boolean values
True and False to these variables in order to make all implications become
logically correct. These problems have many applications involving problems
in which variables may take on either of two values and pairs of variables
are subject to arbitrary constraints; see the Wikipedia article for details.

If G is a graph of this type,
- Symmetrize(G) extends G by adding the contrapositive of each implication
- Satisfiable(G) returns True or False according to whether the
  2SAT instance can be satisfied. It takes linear time in the size of G.
- Forced(G) returns a dictionary mapping a subset of variables of G to
  values that they are forced to hold in any satisfying assignment.
  The empty dictionary is returned if all variables are free to take either
  truth value, and None is returned if the instance is unsatisfiable.
  Because this uses a reachability algorithm in directed acyclic graphs,
  it is not truly linear time but is still polynomial.

D. Eppstein, April 2009.
"""

import unittest
from Not import Not,SymbolicNegation
from Graphs import copyGraph
from StrongConnectivity import Condensation
from AcyclicReachability import Reachability

def Symmetrize(G):
    """Expand implication graph to a larger symmetric form.
    
    If the 2SAT instance includes an implication A=>B, then
    it is also valid to conclude that ~B => ~A, and our 2SAT solver
    needs to have that second implication made explicit.
    But we do not want to force users to supply the contrapositives
    for each of the implications they include, so we use this routine
    to fill in any missing implications.
    """
    H = copyGraph(G)
    for v in G:
        H.setdefault(Not(v),set())  # make sure all negations are included
        for w in G[v]:
            H.setdefault(w,set())   # as well as all implicants
            H.setdefault(Not(w),set()) # and negated implicants
    for v in G:
        for w in G[v]:
            H[Not(w)].add(Not(v))
    return H

def Satisfiable(G):
    """Does this 2SAT instance have a satisfying assignment?"""
    G = Condensation(Symmetrize(G))
    for C in G:
        for v in C:
            if Not(v) in C:
                return False
    return True

def Forced(G):
    """Find forced values for variables in a 2SAT instance.
    
    A variable's value is forced to x if every satisfying assignment
    assigns the same value x to that variable. We return a dictionary
    (possibly empty) in which the keys are the forced variables
    and their values are the values they are forced to.
    
    If the given instance is unsatisfiable, we return None."""
    Force = {}
    Sym = Symmetrize(G)
    Con = Condensation(Sym)
    Map = {}
    for SCC in Con:
        for v in SCC:
            Map[v] = SCC
    Reach = Reachability(Con)
    for v in Sym:
        if Reach.reachable(Map[v],Map[Not(v)]): # v implies not v?
            value = False
            if isinstance(v,SymbolicNegation):
                v = Not(v)
                value = True
            if v in Force:  # already added by negation?
                return None
            Force[v] = value
    return Force

# Unit tests
# Run python TwoSatisfiability.py to perform these tests.

class TwoSatTest(unittest.TestCase):
    T1 = {1:[2,3], 2:[Not(1),3]}
    T2 = {1:[2], 2:[Not(1)], Not(1):[3], 3:[4,2], 4:[1]}

    def testTwoSat(self):
        """Check that the correct problems are satisfiable."""
        self.assertEqual(Satisfiable(self.T1),True)
        self.assertEqual(Satisfiable(self.T2),False)

    def testForced(self):
        """Check that we can correctly identify forced variables."""
        self.assertEqual(Forced(self.T1),{1:False})
        self.assertEqual(Forced(self.T2),None)

if __name__ == "__main__":
    unittest.main()   
