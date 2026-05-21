# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

# You are given two arrays with positive integers arr1 and arr2.

# A prefix of a positive integer is an integer formed by one or more of its digits,
# starting from its leftmost digit. For example, 123 is a prefix of the integer
# 12345, while 234 is not.

# A common prefix of two integers a and b is an integer c, such that c is a prefix
# of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655
# while 1223 and 43456 do not have a common prefix.

# You need to find the length of the longest common prefix between all pairs of
# integers (x, y) such that x belongs to arr1 and y belongs to arr2.

# Return the length of the longest common prefix among all pairs. If no common prefix
# exists among them, return 0.

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for el in arr2:
            str_el = str(el)
            for i in range(len(str_el)):
                prefixes.add(str_el[:i+1])
        res = 0
        for el in arr1:
            str_el = str(el)
            i = 1
            while i <= len(str_el) and str_el[:i] in prefixes:
                res = max(res, i)
                i += 1
    
        return res

# <Medium> Array, Hash Table, String, Trie
# Runtime 328ms 55.71%
# Memory 30.61MB 67.15%
