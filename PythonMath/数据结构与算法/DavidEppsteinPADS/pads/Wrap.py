"""Wrap.py

Break paragraphs into lines, attempting to avoid short lines.

We use the dynamic programming idea of Knuth-Plass to find the
optimal set of breaks according to a penalty function that
penalizes short lines quadratically; this can be done in linear
time via the OnlineConcaveMinima algorithm in SMAWK.py.

D. Eppstein, August 2005.
"""

from SMAWK import OnlineConcaveMinima

def wrap(text,                  # string or unicode to be wrapped
         target = 76,           # maximum length of a wrapped line
         longlast = False,      # True if last line should be as long as others
         frenchspacing = False, # Single space instead of double after periods
         measure = len,         # how to measure the length of a word
         overpenalty = 1000,    # penalize long lines by overpen*(len-target)
         nlinepenalty = 1000,   # penalize more lines than optimal
         onewordpenalty = 25,   # penalize really short last line
         hyphenpenalty = 25):   # penalize breaking hyphenated words
    """Wrap the given text, returning a sequence of lines."""

    # Make sequence of tuples (word, spacing if no break, cum.measure).
    words = []
    total = 0
    spacings = [0, measure(' '), measure('  ')]
    for hyphenword in text.split():
        if words:
            total += spacings[words[-1][1]]
        parts = hyphenword.split('-')
        for word in parts[:-1]:
            word += '-'
            total += measure(word)
            words.append((word,0,total))
        word = parts[-1]
        total += measure(word)
        spacing = 1
        if word.endswith('.') and (len(hyphenword) > 2 or
                                   not hyphenword[0].isupper()):
            spacing = 2 - frenchspacing
        words.append((word,spacing,total))

    # Define penalty function for breaking on line words[i:j]
    # Below this definition we will set up cost[i] to be the
    # total penalty of all lines up to a break prior to word i.
    def penalty(i,j):
        if j > len(words): return -i    # concave flag for out of bounds
        total = cost.value(i) + nlinepenalty
        prevmeasure = i and (words[i-1][2] + spacings[words[i-1][1]])
        linemeasure = words[j-1][2] - prevmeasure
        if linemeasure > target:
            total += overpenalty * (linemeasure - target)
        elif j < len(words) or longlast:
            total += (target - linemeasure)**2
        elif i == j-1:
            total += onewordpenalty
        if not words[j-1][1]:
            total += hyphenpenalty
        return total

    # Apply concave minima algorithm and backtrack to form lines
    cost = OnlineConcaveMinima(penalty,0)
    pos = len(words)
    lines = []
    while pos:
        breakpoint = cost.index(pos)
        line = []
        for i in range(breakpoint,pos):
            line.append(words[i][0])
            if i < pos-1 and words[i][1]:
                line.append(' '*words[i][1])
        lines.append(''.join(line))
        pos = breakpoint
    lines.reverse()
    return lines
