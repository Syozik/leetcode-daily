# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

# Given an array of strings patterns and a string word, return the number of strings
# in patterns that exist as a substring in word.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([pattern in word for pattern in patterns])

# <Easy> Array, String
# Runtime 0ms 100%
# Memory 19.08MB 98.44%
