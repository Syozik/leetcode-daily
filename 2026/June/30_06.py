# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start, end = 0, 0
        ans = 0
        letters = {"a": 0, "b": 0, "c": 0}
        while end < len(s):
            letters[s[end]] += 1
            while letters["a"] and letters["b"] and letters["c"]:
                ans += len(s) - end
                letters[s[start]] -= 1
                start += 1
            end += 1
        return ans

# <Medium> Hash Table, String, Sliding Window
# Runtime  115ms 29.58%
# Memory 19.44MB 48.97%
