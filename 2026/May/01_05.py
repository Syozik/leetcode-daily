# https://leetcode.com/problems/rotate-function

# You are given an integer array nums of length n.

# Assume arrk to be an array obtained by rotating nums by k positions clock-wise.
# We define the rotation function F on nums as follow:
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# Return the maximum value of F(0), F(1), ..., F(n-1).
# The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # for [4, 3, 2, 6]
        # f(0) = 0*4 + 1 * 3 + 2 * 2 + 3 * 6
        # f(1) = 1*4 + 2 * 3 + 3 * 2 + 0*6
        f, total = 1, 0
        for i in range(len(nums)):
            f += nums[i] * i
            total += nums[i]
        max_f = f
        for i in range(len(nums)):
            f = f + total - nums[-1-i] * len(nums)
            max_f = max(f, max_f)

        return max_f

# <Medium> Array, Math, Dynamic Programming
# Runtime 159ms 22.63%
# Memory 31.42MB 22.32%
