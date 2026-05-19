# https://leetcode.com/problems/minimum-common-value
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# return the minimum integer common to both arrays. If there is no common integer
# amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have
# at least one occurrence of that integer.

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1

# <Easy> Array, Hash Table, Two Pointers, Binary Search
# Runtime 9ms 57.54%
# Memory 37.79mb 79.31%
