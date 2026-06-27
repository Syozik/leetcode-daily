# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset

# You are given an array of positive integers nums.

# You need to select a subset of nums which satisfies the following condition:

# You can place the selected elements in a 0-indexed array such that it follows
# the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x]
# (Note that k can be be any non-negative power of 2). For example, [2, 4, 16,
# 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.

# Return the maximum number of elements in a subset that satisfies these conditions.

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        els = defaultdict(int)
        for num in nums:
            els[num] += 1

        ans = max(els[1] - 1 + (els[1] % 2), 1)
        for key, value in els.items():
            if key != 1 and value != 1:
                length = 1
                square = key*key
                while square in els:
                    length += 2
                    if els[square] == 1:
                        break
                    square *= square
                ans = max(ans, length)
        return ans

# <Medium>
# Runtime 106ms 75.59%
# Memory 31.40MB 89.76%
