# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

# Given an array nums, return true if the array was originally sorted
# in non-decreasing order, then rotated some number of positions (including
# zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same
# length such that B[i] == A[(i+x) % A.length] for every valid index i.


class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if rotated:
                    return False
                rotated = True
       
        return not rotated or nums[0] >= nums[-1]

# <Easy> Array
# Runtime 0ms 100%
# Memory 19.10MB 98.41%
