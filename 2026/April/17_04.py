# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description

# You are given an integer array nums.
# A mirror pair is a pair of indices (i, j) such that:
# 0 <= i < j < nums.length, and reverse(nums[i]) == nums[j], where reverse(x)
# denotes the integer formed by reversing the digits of x. Leading zeros are
# omitted after reversing, for example reverse(120) = 21.
# 
# Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j). If no mirror pair exists, return -1.

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            res = 0
            while num:
                res = res * 10 + num % 10
                num //= 10
            return res

        reversed_nums = {}
        res = float("inf")
        for i in range(len(nums)):
            if nums[i] in reversed_nums:
                res = min(res, i - reversed_nums[nums[i]])
        
            reversed_nums[reverse(nums[i])] = i
        return res if res != float("inf") else -1

# Topics: Array, Hash Table, Math

# Runtime 297ms Beats 44.57%
# Memory 41.90mb Beats 73.64%

