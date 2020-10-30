"""FrequencyEstimator.py
Estimate frequencies of items in a data stream.
D. Eppstein, Feb 2016."""

class FrequencyEstimator:
    """Estimate frequencies of a stream of items to a specified accuracy
    (e.g. accuracy=0.1 means within 10% of actual frequency)
    using only O(1/accuracy) bytes of memory."""

    def __init__(self, accuracy):
        self._counts = {}
        self._howmany = int(1./accuracy)
        self._total = 0

    def __iadd__(self, key):
        """FrequencyEstimator += key counts another copy of the key.
        This operation takes amortized constant time, but the worst-case
        time may be O(1/accuracy)."""
        self._total += 1
        if key in self._counts:
            self._counts[key] += 1      # Already there, increment its counter.
        elif len(self._counts) < self._howmany:
            self._counts[key] = 1       # We have room to add it, so do.
        else:        
            # We need to make some room, by decrementing all the counters
            # and clearing out the keys that this reduces to zero.
            # This happens on at most 1/(howmany+1) of the calls to add(),
            # so we have enough (amortized) time to loop over all keys.
            #
            # One complication is that we can't loop over and modify
            # the keys in the dict at the same time, without wasting
            # space making a second list of keys, so instead we build
            # a linked list of keys to eliminate within the dict itself.
            #
            # As a side note, we should not immediately use the space to
            # add the new key. It is not necessary, and makes the data
            # structure less accurate by increasing the potential
            # rate of decrements from 1/(howmany+1) to 1/howmany.
            #
            anchor = linkchain = object()   # nonce sentinel
            for key in self._counts:
                self._counts[key] -= 1
                if self._counts[key] == 0:
                    self._counts[key] = linkchain
                    linkchain = key
            while linkchain != anchor:
                victim, linkchain = linkchain, self._counts[linkchain]
                del self._counts[victim]
        return self

    def __iter__(self):
        """iter(FrequencyEstimator) loops through the most frequent keys."""
        return iter(self._counts)
    
    def __getitem__(self, key):
        """FrequencyEstimator[key] estimates the frequency of the key."""
        if key not in self._counts:
            return 0
        return self._counts[key]*1.0/self._total
