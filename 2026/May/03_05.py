# https://leetcode.com/problems/rotate-string

# Given two strings s and goal, return true if and only if s can become goal after
# some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s*2

# <Easy> String, String Matching
# Runtime 0ms 100%
# Memory 19.29MB 51.56%
