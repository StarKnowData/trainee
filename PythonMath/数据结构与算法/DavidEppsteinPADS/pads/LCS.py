"""LCS.py

Dynamic program for longest common subsequences

D. Eppstein, March 2002.
"""

import unittest


def LongestCommonSubsequence(A,B):
    """Find longest common subsequence of iterables A and B."""
    A = list(A)
    B = list(B)

    # Fill dictionary lcsLen[i,j] with length of LCS of A[:i] and B[:j]
    lcsLen = {}
    for i in range(len(A)+1):
        for j in range(len(B) + 1):
            if i == 0 or j == 0:
                lcsLen[i,j] = 0
            elif A[i-1] == B[j-1]:
                lcsLen[i,j] = lcsLen[i-1,j-1] + 1
            else:
                lcsLen[i,j] = max(lcsLen[i-1,j], lcsLen[i,j-1])

    # Produce actual sequence by backtracking through pairs (i,j),
    # using computed lcsLen values to guide backtracking
    i = len(A)
    j = len(B)
    LCS = []
    while lcsLen[i,j]:
        while lcsLen[i,j] == lcsLen[i-1,j]:
            i -= 1
        while lcsLen[i,j] == lcsLen[i,j-1]:
            j -= 1
        i -= 1
        j -= 1
        LCS.append(A[i])

    LCS.reverse()
    return LCS


# If run standalone, perform unit tests
class LCSTest(unittest.TestCase):
    def testLCS(self):
        A = range(10)
        B = reversed(A)
        self.assertEqual(list(A),LongestCommonSubsequence(A,A))
        self.assertEqual(len(LongestCommonSubsequence(A,B)),1)

if __name__ == "__main__":
    unittest.main()
