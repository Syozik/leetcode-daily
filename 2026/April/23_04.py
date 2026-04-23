# https://leetcode.com/problems/sum-of-distances

# You are given a 0-indexed integer array nums. There exists an array arr of
# length nums.length, where arr[i] is the sum of |i - j| over all j such that
# nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

# Return the array arr.

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        nums_map = defaultdict(list)
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        res = [0] * len(nums)
        for idx_array in nums_map.values():
            if not len(idx_array):
                continue
            total = sum(idx_array)
            prefix = 0
            for i in range(len(idx_array)):
                idx = idx_array[i]
                value = total - prefix - (idx * (len(idx_array) - i))
                value += idx * i - prefix
                prefix += idx
                res[idx] = value
        return res

# <Medium> Topics: Array, Hash Table, Prefix Sum
# Runtime 107ms 92.91%
# Memory 55.78MB 44.49%
