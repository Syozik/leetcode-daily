# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index

# You are given a 0-indexed array nums of n integers and an integer target.
# You are initially positioned at index 0. In one step, you can jump from index i to
# any index j such that:
# 0 <= i < j < n
# -target <= nums[j] - nums[i] <= target

# Return the maximum number of jumps you can make to reach index n - 1.
# If there is no way to reach index n - 1, return -1.

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i):
            if i == len(nums) - 1:
                return 0

            res = -1
            for j in range(i+1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:
                    res = max(res, 1 + dp(j))

            return res if res else -1

        return dp(0)

# <Medium> Array, Dynamic Programming
# Runtime 422ms 70.59%
# Memory 23.56MB 14.38%
