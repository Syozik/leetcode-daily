# https://leetcode.com/problems/count-the-number-of-special-characters-ii

# You are given a string word. A letter c is called special if it appears both in
# lowercase and uppercase in word, and every lowercase occurrence of c appears
# before the first uppercase occurrence of c.

# Return the number of special letters in word.

class Solution:
    def to_lower(self, letter):
        return chr(ord(letter) - ord("A") + ord("a"))

    def numberOfSpecialChars(self, word: str) -> int:
        last_occurence = {}
        for i, letter in enumerate(word):
            if "a" <= letter <= "z":
                last_occurence[letter] = i

        n, seen, count = len(word), set(), 0
        for i, letter in enumerate(word):
            if "A" <= letter <= "Z" and letter not in seen:
                if last_occurence.get(self.to_lower(letter), n) < i:
                    count += 1
                seen.add(letter)
        return count

# <Medium> Hash Table, String
# Runtime 404ms 17.06%
# Memory 21.69% 28.82%
