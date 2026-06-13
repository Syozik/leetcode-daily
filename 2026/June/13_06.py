# https://leetcode.com/problems/weighted-word-mapping

# You are given an array of strings words, where each string represents a word containing
# lowercase English letters.
# You are also given an integer array weights of length 26, where weights[i] represents the
# weight of the ith lowercase English letter.
# The weight of a word is defined as the sum of the weights of its characters.

# For each word, take its weight modulo 26 and map the result to a lowercase English letter
# using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').

# Return a string formed by concatenating the mapped characters for all words in order.

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a, z = ord("a"), ord("z")
        def get_weight(word):
            weight = 0
            for letter in word:
                weight += weights[ord(letter) - a]
            return weight % 26

        res = ""
        for word in words:
            res += chr(z - get_weight(word))
        return res

# <Easy> Array, String, Simulation
# Runtime 8ms 64.03%
# Memory 19.27MB 72.25%
