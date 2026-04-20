# https://leetcode.com/problems/two-furthest-houses-with-different-colors

# There are n houses evenly lined up on the street, and each house is beautifully
# painted. You are given a 0-indexed integer array colors of length n, where
# colors[i] represents the color of the ith house.
# Return the maximum distance between two houses with different colors.

# O(n^2)
# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         res = 0
#         for i in range(len(colors)):
#             j = len(colors) - 1
#             while j > i and colors[j] == colors[i]:
#                 j -= 1
#             res = max(res, j - i)
#         return res

# or O(n)

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i, j = 0, len(colors) - 1
        while colors[i] == colors[-1]:
            i += 1
        
        while colors[j] == colors[0]:
            j -= 1

        return max(j, len(colors) - i - 1)

# <Easy> Topics: Array, Greedy
# Runtime 0ms 100%
# Memory 19.26mb 61.41%

