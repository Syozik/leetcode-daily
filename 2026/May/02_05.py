# https://leetcode.com/problems/rotated-digits

# An integer x is a good if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from x. Each digit must be rotated - we
# cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For example:
# - 0, 1, and 8 rotate to themselves,
# - 2 and 5 rotate to each other (in this case they are rotated in a different
# direction, in other words, 2 or 5 gets mirrored),
# - 6 and 9 rotate to each other, and
# - the rest of the numbers do not rotate to any other number and become invalid.

# Given an integer n, return the number of good integers in the range [1, n].

class Solution:
    same = set([0, 1, 8])
    mirrored = set([2, 5, 6, 9])

    def isGood(self, n):
        changed = False
        while n:
            digit = n%10
            n = n // 10
            if digit in self.same:
                continue
            if digit in self.mirrored:
                changed = True
            else:
                return False
        return changed

    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if self.isGood(i):
                res += 1
        return res

# <Medium> Math, Dynamic Programming
# Runtime 23ms 66.55%
# Memory 19.24mb 69.59%
