# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii

# You are given a string word containing lowercase English letters.
# Telephone keypads have keys mapped with distinct collections of lowercase English
# letters, which can be used to form words by pushing them. For example, the key
# 2 is mapped with ["a","b","c"], we need to push the key one time to type "a",
# two times to type "b", and three times to type "c" .

# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
# The keys can be remapped to any amount of letters, but each letter must be mapped
# to exactly one key. You need to find the minimum number of times the keys will be
# pushed to type the string word.

# Return the minimum number of pushes needed to type word after remapping the keys.
# Note that 1, *, #, and 0 do not map to any letters.

class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = [0]*26
        a = ord("a")
        for letter in word:
            letters[ord(letter) - a] += 1

        letters.sort(reverse=True)

        ans, length = 0, 0
        for i in range(26):
            if letters[i]:
                ans += letters[i] * ((length // 8) + 1)
                length += 1

        return ans

# <Medium> Hash Table, String, Greedy, Sorting, Counting
# Runtime 153ms 44.15%
# Memory 19.83MB 93.65%
