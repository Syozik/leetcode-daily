# https://leetcode.com/problems/count-the-number-of-special-characters-i

# You are given a string word. A letter is called special if it appears both in
# lowercase and uppercase in word.

# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count, lower, upper = 0, set(), set()
        for letter in word:
            if letter in lower or letter in upper:
                continue
            if "a" <= letter <= "z":
                if chr(ord(letter) + ord("A") - ord("a")) in upper:
                    count += 1
                lower.add(letter)
            else:
                if chr(ord(letter) - ord("A") + ord("a")) in lower:
                    count += 1
                upper.add(letter) 

        return count

# <Easy> Hash Table, String
# Runtime 3ms 37%
# Memory 19.28mb 64.16%
