# https://leetcode.com/problems/smallest-stable-index-i

# You are given an integer array nums of length n and an integer k.

# For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).
# An index i is called stable if its instability score is less than or equal to k.
# Return the smallest stable index. If no such index exists, return -1.

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        prefix, suffix = [nums[0]], [nums[-1]]
        for i in range(1, n):
            prefix.append(max(prefix[-1], nums[i]))
            suffix.append(min(suffix[-1], nums[n-1-i]))

        for i in range(n):
            if prefix[i] - suffix[n-1-i] <= k:
                return i
        return -1

# <Easy> Array, Prefix Sum
# Runtime 4ms 58.13%
# Memory 19.27MB 71.43%
