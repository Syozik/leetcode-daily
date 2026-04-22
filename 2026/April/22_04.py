# https://leetcode.com/problems/words-within-two-edits-of-dictionary

# You are given two string arrays, queries and dictionary. All words in each
# array comprise of lowercase English letters and have the same length.

# In one edit you can take a word from queries, and change any letter in it to
# any other letter. Find all words from queries that, after a maximum of two
# edits, equal some word from dictionary.

# Return a list of all words from queries, that match with some word from
# dictionary after a maximum of two edits. Return the words in the same order
# they appear in queries.

class Solution:
     def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            shouldAdd = False
            for word in dictionary:
                difference = 0
                for i in range(len(word)):
                    if word[i] != query[i]:
                        difference += 1
                    if difference > 2:
                        break
                else:
                    shouldAdd = True
                    break

            if shouldAdd:
                ans.append(query)

        return ans

# <Medium> Topics: Array, String, Trie
# Runtime 4ms 98.04%
# Memory 19.18MB 100%

