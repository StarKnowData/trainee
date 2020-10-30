"""Not.py

Symbolic negation operator.

For any Python value x, Not(x) is an object, with the properties that
    Not(x)==Not(y) iff x==y
    Not(Not(x))==x.
If x is hashable, so is Not(x).

The purpose of this is to use within TwoSatisfiability and similar code,
to allow Python objects to represent logical variables. If x is an object representing a variable, Not(x) can be used to represent its negation.

To determine whether a given object y is of the form Not(x), use
isinstance(y,SymbolicNegation).  If it is, you can recover x as Not(y).

D. Eppstein, April 2009.
"""

import unittest

class DoubleNegationError(Exception): pass

class SymbolicNegation:
    def __init__(self,x):
        if isinstance(x,SymbolicNegation):
            raise DoubleNegationError(
              "Use Not(x) rather than instantiating SymbolicNegation directly")
        self.negation = x

    def negate(self):
        return self.negation
        
    def __repr__(self):
        return "Not(" + repr(self.negation) + ")"

    def __eq__(self,other):
        return isinstance(other,SymbolicNegation) and \
               self.negation == other.negation

    def __hash__(self):
        return -hash(self.negation)

def Not(x):
    if isinstance(x,SymbolicNegation):
        return x.negate()
    else:
        return SymbolicNegation(x)

class NotNotTest(unittest.TestCase):
    things = [None,3,"ABC",Not(27)]
    def testNot(self):
        for x in NotNotTest.things:
            self.assertEqual(Not(Not(x)),x)
    def testEq(self):
        for x in NotNotTest.things:
            for y in NotNotTest.things:
                self.assertEqual(Not(x)==Not(y),x==y)
    def testHash(self):
        D = {Not(x):x for x in NotNotTest.things}
        for x in NotNotTest.things:
            self.assertEqual(D[Not(x)],x)

if __name__ == "__main__":
    unittest.main()   
