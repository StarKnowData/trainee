"""Automata.py

Manipulation of and conversions between regular expressions,
deterministic finite automata, and nondeterministic finite automata.

D. Eppstein, UC Irvine, November 2003.
"""

from Util import arbitrary_item

import sys
import operator
import unittest

from PartitionRefinement import PartitionRefinement
from Sequence import Sequence

# Hack for Python 3 compatibility
try:
    unicode
except:
    unicode = str

class LanguageError(Exception): pass

def Language(A):
    """Convert automaton A into an object describing its language.
    This is distinct from class RegularLanguage in case we
    want to later add other types of automaton and nonregular languages.
    """
    return A.language()

class RegularLanguage:
    """Object representing the language recognized by a DFA or NFA.
    Available operations are testing whether a string is in the language,
    logical combinations, and subset and equality testing.
    """
    def __init__(self,arg):
        if isinstance(arg,FiniteAutomaton):
            self.recognizer = arg
        elif isinstance(arg,(str,unicode)):
            self.recognizer = RegExp(arg)
        else:
            raise LanguageError("Unrecognized constructor for RegularLanguage")

    def __contains__(self,inputsequence):
        return self.recognizer(inputsequence)

    def __eq__(self,other):
        if not isinstance(other,RegularLanguage):
            return None
        return self.recognizer.minimize() == other.recognizer.minimize()

    def __ne__(self,other):
        return not (self == other)

    def __le__(self,other):
        return not(self &~ other)

    def __ge__(self,other):
        return not(other &~ self)

    def __lt__(self,other):
        return self <= other and self != other

    def __gt__(self,other):
        return self >= other and self != other

    def __invert__(self):
        """Complement (with respect to alphabet) of language."""
        return Language(self.recognizer.complement())

    def __and__(self,other):
        """Intersection of two languages with the same alphabet."""
        if not isinstance(other,RegularLanguage):
            raise LanguageError("Unable to intersect nonregular language")
        return Language(self.recognizer.intersection(other.recognizer))

    def __or__(self,other):
        """Union of two languages with the same alphabet."""
        if not isinstance(other,RegularLanguage):
            raise LanguageError("Unable to intersect nonregular language")
        return Language(self.recognizer.union(other.recognizer))

    def __xor__(self,other):
        """Symmetric difference of two languages with the same alphabet."""
        if not isinstance(other,RegularLanguage):
            raise LanguageError("Unable to intersect nonregular language")
        return Language(self.recognizer.symmetricDifference(other.recognizer))

    def __nonzero__(self):
        """Is this the empty language?"""
        for x in self.recognizer.states():
            if x.isfinal():
                return True
        return False

class FiniteAutomaton:
    """Base class for DFA and NFA.  This class should not be instantiated
    on its own, but dispatches methods that are appropriate to both types
    of automaton by calling .asDFA() or .asNFA() to convert the automaton
    to the appropriate type.  All automaton instances should include the
    following instance variables and methods:
     - x.initial: initial state (for DFA) or set of states (for NFA)
     - x.alphabet: set of input symbols accepted by the automaton
     - x.transition(state,symbol): result of transition function,
       either a single state (for a DFA) or set of states (for an NFA)
     - x.isfinal(state): whether the state is an accepting state
     - x.asDFA(): return an equivalent DFA
     - x.asNFA(): return an equivalent NFA
    """

    initial = alphabet = transition = isfinal = asDFA = asNFA = None

    def __len__(self):
        """How many states does this automaton have?"""
        return len(list(self.states()))

    def __call__(self,symbols):
        """Test whether sequence of symbols is accepted by the DFA."""
        return self.asDFA()(symbols)

    def language(self):
        """Form language object for language recognized by automaton."""
        return RegularLanguage(self)

    def states(self):
        """Generate all states reachable from initial state."""
        return self.asNFA().states()

    def pprint(self,output=sys.stdout):
        """Pretty-print this automaton to an output stream."""
        return self.asNFA().pprint(output)

    def minimize(self):
        """Return smallest equivalent DFA."""
        return _MinimumDFA(self.asDFA())

    def reverse(self):
        """Construct NFA for reversal of original NFA's language."""
        return _ReverseNFA(self.asNFA())

    def renumber(self,offset=0):
        """Replace complicated state objects by small integers."""
        return _RenumberNFA(self.asNFA(),offset=offset)

    def RegExp(self):
        """Return equivalent regular expression."""
        return self.asNFA().RegExp()

    def complement(self):
        """Make automaton recognizing complement of given automaton's language."""
        return _ComplementDFA(self.asDFA())

    def union(self,other):
        """Make automaton recognizing union of two automata's languages."""
        return _ProductDFA(self.asDFA(),other.asDFA(),operator.or_)

    def intersection(self,other):
        """Make automaton recognizing union of two automata's languages."""
        return _ProductDFA(self.asDFA(),other.asDFA(),operator.and_)

    def symmetricDifference(self,other):
        """Make automaton recognizing union of two automata's languages."""
        return _ProductDFA(self.asDFA(),other.asDFA(),operator.xor)

class DFA(FiniteAutomaton):
    """Base class for deterministic finite automaton.  Subclasses are
    responsible for filling out the details of the initial state, alphabet,
    and transition function.
    """
    def asDFA(self):
        return self

    def asNFA(self):
        return _NFAfromDFA(self)

    def __call__(self,symbols):
        """Test whether sequence of symbols is accepted by the DFA."""
        state = self.initial
        for symbol in symbols:
            if symbol not in self.alphabet:
                raise LanguageError("Symbol " + repr(symbol) +
                                 " not in input alphabet")
            state = self.transition(state,symbol)
        return self.isfinal(state)

    def __eq__(self,other):
        """Report whether these two DFAs have equivalent states."""
        if not isinstance(other,DFA) or len(self) != len(other) \
                or self.alphabet != other.alphabet:
            return False
        equivalences = {self.initial:other.initial}
        unprocessed = [self.initial]
        while unprocessed:
            x = unprocessed.pop()
            y = equivalences[x]
            for c in self.alphabet:
                xc = self.transition(x,c)
                yc = other.transition(y,c)
                if xc not in equivalences:
                    equivalences[xc] = yc
                    unprocessed.append(xc)
                elif equivalences[xc] != yc:
                    return False
        return True

    def __ne__(self,other):
        """Report whether these two DFAs have equivalent states."""
        return not (self == other)

class NFA(FiniteAutomaton):
    """Base class for nondeterministic finite automaton.  Subclasses are
    responsible for filling out the details of the initial state, alphabet,
    and transition function.  Note that the NFAs defined here do not allow
    epsilon-transitions.  Results of self.initial and self.transition are
    assumed to be represented as frozenset instances.
    """
    def asNFA(self):
        return self

    def asDFA(self):
        return _DFAfromNFA(self)

    def states(self):
        visited = set()
        unvisited = set(self.initial)
        while unvisited:
            state = arbitrary_item(unvisited)
            yield state
            unvisited.remove(state)
            visited.add(state)
            for symbol in self.alphabet:
                unvisited |= self.transition(state,symbol) - visited

    def pprint(self,output=sys.stdout):
        """Pretty-print this NFA to an output stream."""
        for state in self.states():
            adjectives = []
            if state in self.initial:
                adjectives.append("initial")
            if self.isfinal(state):
                adjectives.append("accepting")
            if not [c for c in self.alphabet if self.transition(state,c)]:
                adjectives.append("terminal")
            if not adjectives:
                print >>output, state
            else:
                print >>output, state, "(" + ", ".join(adjectives) + ")"
            for c in self.alphabet:
                for neighbor in self.transition(state,c):
                    print >>output, "  --[" + str(c) + "]-->", neighbor

    def RegExp(self):
        """Convert to regular expression and return as a string.
        See Sipser for an explanation of this algorithm."""

        # create artificial initial and final states
        initial = object()
        final = object()
        states = {initial,final} | set(self.states())

        # 2d matrix of expressions connecting each pair of states
        expr = {}
        for x in states:
            for y in states:
                expr[x,y] = None
        for x in self.states():
            if x in self.initial:
                expr[initial,x] = ''
            if self.isfinal(x):
                expr[x,final] = ''
            expr[x,x] = ''
        for x in self.states():
            for c in self.alphabet:
                for y in self.transition(x,c):
                    if expr[x,y]:
                        expr[x,y] += '+' + str(c)
                    else:
                        expr[x,y] = str(c)

        # eliminate states one at a time
        for s in self.states():
            states.remove(s)
            for x in states:
                for y in states:
                    if expr[x,s] is not None and expr[s,y] is not None:
                        xsy = []
                        if expr[x,s]:
                            xsy += self._parenthesize(expr[x,s])
                        if expr[s,s]:
                            xsy += self._parenthesize(expr[s,s],True) + ['*']
                        if expr[s,y]:
                            xsy += self._parenthesize(expr[s,y])
                        if expr[x,y] is not None:
                            xsy += ['+',expr[x,y] or '()']
                        expr[x,y] = ''.join(xsy)
        return expr[initial,final]

    def _parenthesize(self,expr,starring=False):
        """Return list of strings with or without parens for use in RegExp.
        This is only for the purpose of simplifying the expressions returned,
        by omitting parentheses or other expression features when unnecessary;
        it would always be correct simply to return ['(',expr,')'].
        """
        if len(expr) == 1 or (not starring and '+' not in expr):
            return [expr]
        elif starring and expr.endswith('+()'):
            return ['(',expr[:-3],')']  # +epsilon redundant when starring
        else:
            return ['(',expr,')']

class _DFAfromNFA(DFA):
    """Conversion of NFA to DFA.  We create a DFA state for each set
    of NFA states. A DFA state is final if it contains at least one
    final NFA set, and the transition function for a DFA state is the
    union of the transition functions of the NFA states it contains.
    """
    def __init__(self,N):
        self.initial = frozenset(N.initial)
        self.alphabet = N.alphabet
        self.NFA = N

    def transition(self,stateset,symbol):
        result = set()
        for state in stateset:
            result |= self.NFA.transition(state,symbol)
        return frozenset(result)

    def isfinal(self,stateset):
        for state in stateset:
            if self.NFA.isfinal(state):
                return True
        return False

class _NFAfromDFA(NFA):
    """Conversion of DFA to NFA.  We convert the initial state and the
    results of each transition function into single-element sets.
    """
    def __init__(self,D):
        self.initial = frozenset([D.initial])
        self.alphabet = D.alphabet
        self.DFA = D

    def transition(self,state,symbol):
        return frozenset([self.DFA.transition(state,symbol)])

    def isfinal(self,state):
        return self.DFA.isfinal(state)

class RegExp(NFA):
    """Convert regular expression to NFA."""

    def __init__(self,expr):
        self.expr = expr
        self.pos = 0
        self.nstates = 0
        self.expect = {}
        self.successor = {}
        self.alphabet = set()
        self.initial,penultimate,epsilon = self.expression()
        final = self.newstate(None)
        for state in penultimate:
            self.successor[state].add(final)
        self.final = frozenset([final])
        if epsilon:
            self.final = self.final | self.initial

    def transition(self,state,c):
        """Implement NFA transition function."""
        if c != self.expect[state]:
            return frozenset()
        else:
            return self.successor[state]

    def isfinal(self,state):
        """Implement NFA acceptance test."""
        return state in self.final

    # Recursive-descent parser for regular expressions.
    # Each function uses self.pos as a pointer into self.expr,
    # updates self.expect and self.successor,
    # and returns a tuple (initial,penultimate,epsilon), where
    #   initial = the initial states of the subexpression
    #   penultimate = states one step away from an accepting state
    #   epsilon = true if the subexpression accepts the empty string

    def epsilon(self):
        """Parse an empty string and return an empty automaton."""
        return frozenset(),frozenset(),True

    def newstate(self,expect):
        """Allocate a new state in which we expect to see the given letter."""
        state = self.nstates
        self.successor[state] = set()
        self.expect[state] = expect
        self.nstates += 1
        return state

    def base(self):
        """Parse a subexpression that can be starred: single letter or group."""
        if self.pos == len(self.expr) or self.expr[self.pos] == ')':
            return self.epsilon()
        if self.expr[self.pos] == '(':
            self.pos += 1
            ret = self.expression()
            if self.pos == len(self.expr) or self.expr[self.pos] != ')':
                raise LanguageError("Close paren expected at char " + str(self.pos))
            self.pos += 1
            return ret
        if self.expr[self.pos] == '\\':
            self.pos += 1
            if self.pos == len(self.expr):
                raise RegExpError("Character expected after backslash")
        self.alphabet.add(self.expr[self.pos])
        state = self.newstate(self.expr[self.pos])
        self.pos += 1
        state = frozenset([state])
        return state,state,False

    def factor(self):
        """Parse a catenable expression: base or starred base."""
        initial,penultimate,epsilon = self.base()
        while self.pos < len(self.expr) and self.expr[self.pos] == '*':
            self.pos += 1
            for state in penultimate:
                self.successor[state] |= initial
            epsilon = True
        return initial,penultimate,epsilon

    def term(self):
        """Parse a summable expression: factor or concatenation."""
        initial,penultimate,epsilon = self.factor()
        while self.pos < len(self.expr) and self.expr[self.pos] not in ')+':
            Fi,Fp,Fe = self.factor()
            for state in penultimate:
                self.successor[state] |= Fi
            if epsilon:
                initial = initial | Fi
            if Fe:
                penultimate = penultimate | Fp
            else:
                penultimate = Fp
            epsilon = epsilon and Fe
        return initial,penultimate,epsilon

    def expression(self):
        """Parse a whole regular expression or grouped subexpression."""
        initial,penultimate,epsilon = self.term()
        while self.pos < len(self.expr) and self.expr[self.pos] == '+':
            self.pos += 1
            Ti,Tp,Te = self.term()
            initial = initial | Ti
            penultimate = penultimate | Tp
            epsilon = epsilon or Te
        return initial,penultimate,epsilon

class LookupNFA(NFA):
    """Construct NFA with precomputed lookup table of transitions."""
    def __init__(self,alphabet,initial,ttable,final):
        self.alphabet = alphabet
        self.initial = frozenset(initial)
        self.ttable = ttable
        self.final = frozenset(final)

    def transition(self,state,symbol):
        return frozenset(self.ttable[state,symbol])

    def isfinal(self,state):
        return state in self.final

def _RenumberNFA(N,offset=0):
    """Replace NFA state objects with small integers."""
    replacements = {}
    for x in N.states():
        replacements[x] = offset
        offset += 1
    initial = [replacements[x] for x in N.initial]
    ttable = {}
    for state in N.states():
        for symbol in N.alphabet:
            ttable[replacements[state],symbol] = [replacements[x]
                for x in N.transition(state,symbol)]
    final = [replacements[x] for x in N.states() if N.isfinal(x)]
    return LookupNFA(N.alphabet,initial,ttable,final)

class _ProductDFA(DFA):
    """DFA that simulates D1 and D2 and combines their outputs with op."""
    def __init__(self,D1,D2,op):
        if D1.alphabet != D2.alphabet:
            raise LanguageError("DFAs have incompatible alphabets")
        self.alphabet = D1.alphabet
        self.initial = (D1.initial,D2.initial)
        self.D1 = D1
        self.D2 = D2
        self.op = op

    def transition(self,state,symbol):
        s1,s2 = state
        return self.D1.transition(s1,symbol), \
               self.D2.transition(s2,symbol)

    def isfinal(self,state):
        s1,s2 = state
        f1 = self.D1.isfinal(s1) and 1 or 0
        f2 = self.D2.isfinal(s2) and 1 or 0
        return self.op(f1,f2)

def _ReverseNFA(N):
    """Construct NFA for reversal of original NFA's language."""
    initial = [s for s in N.states() if N.isfinal(s)]
    ttable = {(s,c):[] for s in N.states() for c in N.alphabet}
    for s in N.states():
        for c in N.alphabet:
            for t in N.transition(s,c):
                ttable[t,c].append(s)
    return LookupNFA(N.alphabet,initial,ttable,N.initial)

class _ComplementDFA(DFA):
    """DFA for complementary language."""
    def __init__(self,D):
        self.DFA = D
        self.initial = D.initial
        self.alphabet = D.alphabet

    def transition(self,state,symbol):
        return self.DFA.transition(state,symbol)

    def isfinal(self,state):
        return not self.DFA.isfinal(state)

class _MinimumDFA(DFA):
    """Construct equivalent DFA with minimum number of states,
    using Hopcroft's O(ns log n) partition-refinement algorithm.
    """
    def __init__(self,D):
        # refine partition of states by reversed neighborhoods
        N = D.reverse()
        P = PartitionRefinement(D.states())
        P.refine([s for s in D.states() if D.isfinal(s)])
        unrefined = Sequence(P,key=id)
        while unrefined:
            part = arbitrary_item(unrefined)
            unrefined.remove(part)
            for symbol in D.alphabet:
                neighbors = set()
                for state in part:
                    neighbors |= N.transition(state,symbol)
                for new,old in P.refine(neighbors):
                    if old in unrefined or len(new) < len(old):
                        unrefined.append(new)
                    else:
                        unrefined.append(old)

        # convert partition to DFA
        P.freeze()
        self.partition = P
        self.initial = P[D.initial]
        self.alphabet = D.alphabet
        self.DFA = D

    def transition(self,state,symbol):
        rep = arbitrary_item(state)
        return self.partition[self.DFA.transition(rep,symbol)]

    def isfinal(self,state):
        rep = arbitrary_item(state)
        return self.DFA.isfinal(rep)

# If called as standalone routine, run some unit tests

class RegExpTest(unittest.TestCase):
    # tuples (L,[strings in L],[strings not in L])
    languages = [
        (RegularLanguage("0"), ["0"], ["","00"]),
        (RegularLanguage("(10+0)*"), ["","0","010"], ["1"]),
        (RegularLanguage("(0+1)*1(0+1)(0+1)"), ["000100"], ["0011"]),
    ]

    def testMembership(self):
        """membership tests for RegularLanguage(expression)"""
        for L,Li,Lx in self.languages:
            for S in Li:
                self.assertTrue(S in L)
            for S in Lx:
                self.assertTrue(S not in L)

    def testComplement(self):
        """membership tests for ~RegularLanguage"""
        for L,Li,Lx in self.languages:
            L = ~L
            for S in Lx:
                self.assertTrue(S in L)
            for S in Li:
                self.assertTrue(S not in L)

    def testEquivalent(self):
        """test that converting NFA->expr->NFA produces same language"""
        for L1,Li,Lx in self.languages:
            L2 = RegularLanguage(L1.recognizer.RegExp())
            self.assertEqual(L1,L2)

    def testInequivalent(self):
        """test that different regular languages are recognized as different"""
        for i in range(len(self.languages)):
            for j in range(i):
                self.assertNotEqual(self.languages[i][0],
                                    self.languages[j][0])

if __name__ == "__main__":
    unittest.main()   

