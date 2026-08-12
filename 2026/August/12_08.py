# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called good if the frequency of each element in this array is less
# than or equal to k.
# Return the length of the longest good subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        max_freq, max_len = None, 0
        l, r = 0, 0
        while r < len(nums):
            freq[nums[r]] += 1
            if freq[max_freq] < freq[nums[r]]:
                max_freq = nums[r]
            while freq[max_freq] > k:
                freq[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r-l + 1)
            r += 1

        return max_len

# <Medium> Array, Hash Table, Sliding Window 
# Runtime 320ms 13.37%
# Memory 35.38MB 38.32%
