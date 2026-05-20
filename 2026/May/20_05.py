# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays

# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to
# the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from
# 1 to n exactly once.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        set_a, set_b = set(), set()
        for i in range(len(A)):
            if A[i] == B[i]:
                res.append(res[-1] + 1 if res else 1)
            else:
                set_b.add(B[i])
                set_a.add(A[i])
                prefix = res[-1] if res else 0
                if A[i] in set_b:
                    prefix += 1
                if B[i] in set_a:
                    prefix += 1
                res.append(prefix)
        return res

# <Medium> 
# Runtime 6ms 70.57%
# Memory 19.26MB 73.05%
