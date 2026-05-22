# https://leetcode.com/problems/search-in-rotated-sorted-array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown
# index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become
# [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        if target >= nums[0]:
            l, r = 0, l
        else:
            l, r = l, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

# <Medium> Array, Binary Search
# Runtime 0ms 100%
# Memory 19.49MB 39.04%
