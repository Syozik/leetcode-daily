# https://leetcode.com/problems/smallest-palindromic-rearrangement-i

# You are given a palindromic string s.
# Return the lexicographically smallest palindromic permutation of s.

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1
        a = ord("a")
        res = ""
        remaining = None
        for i in range(26):
            letter = chr(a+i)
            while letters[letter]:
                if letters[letter] == 1:
                    remaining = letter
                    letters[letter] = 0
                else:
                    res += letter
                    letters[letter] -= 2
        return res + (remaining or "") + res[::-1]

# <Medium> String, Sorting, Counting Sort
# Runtime 601ms 9.22%
# Memory 21.14MB 34.56%
