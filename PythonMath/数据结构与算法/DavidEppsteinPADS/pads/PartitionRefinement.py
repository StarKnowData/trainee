"""PartitionRefinement.py

Maintain and refine a partition of a set of items into subsets,
as used e.g. in Hopcroft's DFA minimization algorithm,
modular decomposition of graphs, etc.

D. Eppstein, November 2003.
"""

class PartitionError(Exception): pass

class PartitionRefinement:
    """Maintain and refine a partition of a set of items into subsets.
    Space usage for a partition of n items is O(n), and each refine
    operation takes time proportional to the size of its argument.
    """

    def __init__(self,items):
        """Create a new partition refinement data structure for the given
        items.  Initially, all items belong to the same subset.
        """
        S = set(items)
        self._sets = {id(S):S}
        self._partition = {x:S for x in S}

    def __getitem__(self,element):
        """Return the set that contains the given element."""
        return self._partition[element]

    def __iter__(self):
        """Loop through the sets in the partition."""
        try:    # Python 2/3 compatibility
            return self._sets.itervalues()
        except AttributeError:
            return iter(self._sets.values())

    def __len__(self):
        """Return the number of sets in the partition."""
        return len(self._sets)

    def add(self,element,theset):
        """Add a new element to the given partition subset."""
        if id(theset) not in self._sets:
            raise PartitionError("Set does not belong to the partition")
        if element in self._partition:
            raise PartitionError("Element already belongs to the partition")
        theset.add(element)
        self._partition[element] = theset

    def remove(self,element):
        """Remove the given element from its partition subset."""
        self._partition[element].remove(element)
        del self._partition[element]

    def refine(self,S):
        """Refine each set A in the partition to the two sets
        A & S, A - S.  Return a list of pairs (A & S, A - S)
        for each changed set.  Within each pair, A & S will be
        a newly created set, while A - S will be a modified
        version of an existing set in the partition.
        Not a generator because we need to perform the partition
        even if the caller doesn't iterate through the results.
        """
        hit = {}
        output = []
        for x in S:
            if x in self._partition:
                Ax = self._partition[x]
                hit.setdefault(id(Ax),set()).add(x)
        for A,AS in hit.items():
            A = self._sets[A]
            if AS != A:
                self._sets[id(AS)] = AS
                for x in AS:
                    self._partition[x] = AS
                A -= AS
                output.append((AS,A))
        return output

    def freeze(self):
        """Make all sets in S immutable."""
        for S in list(self._sets.values()):
            F = frozenset(S)
            for x in F:
                self._partition[x] = F
            self._sets[id(F)] = F
            del self._sets[id(S)]
