# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums
# such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater
# than pivot.
# The relative order of the elements less than pivot and the elements greater than
# pivot is maintained.

# More formally, consider every pi, pj where pi is the new position of the ith
# element and pj is the new position of the jth element. If i < j and both elements
# are smaller (or larger) than pivot, then pi < pj.

# Return nums after the rearrangement.

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, after = [], []
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)
        return before + [pivot]*(len(nums) - len(before) - len(after)) + after

# <Medium> Array, Two Pointers, Simulation
# Runtime 14ms 97.42%
# Memory 33.62MB 77.63%
