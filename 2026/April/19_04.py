# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

# You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
# A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length
# is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i.
# Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def bin_search(i):
            l, r = i, len(nums2)
            while l < r:
                m = (l+r)//2
                if nums2[m] >= nums1[i]:
                    l = m+1
                else:
                    r = m
            return l - 1

        res = 0
        for i in range(min(len(nums2), len(nums1))):
            if nums1[i] > nums2[i]:
                continue
            j = bin_search(i)
            res = max(res, j - i)

        return res 

# <Medium> Topics: Array, Two Pointers, Binary Search
# Runtime 362ms 22.68%, Memory 36.07MB 41.58%

# Another solution if the array aren't non-increasing is to make the suffix
# array out of the nums2:
for i in range(len(nums2)-2, -1, -1):
    nums2[i] = max(nums2[i], nums2[i+1])

