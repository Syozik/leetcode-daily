# https://leetcode.com/problems/check-if-array-is-good

# You are given an integer array nums. We consider an array good if it is a permutation
# of an array base[n].
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1
# which contains 1 to n - 1 exactly once, plus two occurrences of n).
# For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

# Return true if the given array is good, otherwise return false.
# Note: A permutation of integers represents an arrangement of these numbers.

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        set_nums = set(range(1, len(nums)))
        seen = False
        for num in nums:
            if num not in set_nums:
                if num == len(nums) - 1:
                    if seen:
                        return False
                    seen = True
                else:
                    return False
            else:
                set_nums.remove(num)
        return seen

# <Easy> Array, Hash Table, Sorting
# Runtime 0ms 100%
# Memory 19.38mb 17.79%
