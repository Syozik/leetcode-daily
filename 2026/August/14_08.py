# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences
# Given a string s, return the maximum length of a substring such that it
# contains at most two occurrences of each character.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l, res = 0, 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res

# <Easy> Hash Table, String, Sliding Window
# Runtime 3ms 76.16%
# Memory 19.17MB 88.83%
