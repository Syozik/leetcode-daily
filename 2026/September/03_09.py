# https://leetcode.com/problems/construct-uniform-parity-array-ii

# You are given an array nums1 of n distinct integers.

# You want to construct another array nums2 of length n such that the elements
# in nums2 are either all odd or all even.

# For each index i, you must choose exactly one of the following (in any order):

# - nums2[i] = nums1[i]
# - nums2[i] = nums1[i] - nums1[j], for an index j != i: nums1[i] - nums1[j] >= 1
# Return true if it is possible to construct such an array, otherwise return false.

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        has_odd, has_even = False, False
        odd, even = True, True
        for num in nums1:
            if num % 2:
                if not has_odd:
                    even = False
                has_odd = True
            else:
                if not has_odd:
                    odd = False
                has_even = True
        return odd or even

# <Medium> Array, Math
# Runtime 32.32%
# Memory 51.83%
