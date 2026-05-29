# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum

# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float("inf")
        for num in nums:
            curr_sum = 0
            while num:
                curr_sum += num % 10
                num //= 10
            min_sum = min(min_sum, curr_sum)
        return min_sum

# <Easy> Array, Math
# Runtime 4ms 51.47%
# Memory 19.25MB 56.38%
