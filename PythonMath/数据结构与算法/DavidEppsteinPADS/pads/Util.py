"""Util.py

Simple utility functions for PADS library.
D. Eppstein, April 2004.
"""

def arbitrary_item(S):
    """
    Select an arbitrary item from set or sequence S.
    Avoids bugs caused by directly calling iter(S).next() and
    mysteriously terminating loops in callers' code when S is empty.
    """
    try:
        return next(iter(S))
    except StopIteration:
        raise IndexError("No items to select.")

def map_to_constant(constant):
    """
    Return a factory that turns sequences into dictionaries, where the
    dictionary maps each item in the sequence into the given constant.
    Appropriate as the adjacency_list_type argument for Graphs.copyGraph.
    """
    def factory(seq):
        return dict.fromkeys(seq,constant)
    return factory
