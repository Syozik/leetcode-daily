# https://leetcode.com/problems/mirror-distance-of-an-integer

# You are given an integer n.
# Define its mirror distance as: abs(n - reverse(n)) where reverse(n) is the
# integer formed by reversing the digits of n.
# Return an integer denoting the mirror distance of n.

def reverse(n):
    res = 0
    while n:
        res = res * 10 + n%10
        n //= 10
    return res

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - reverse(n))

# <Easy> Topics: Math
# Runtime 0ms 100%
# Memory 19.3MB 56.37%
