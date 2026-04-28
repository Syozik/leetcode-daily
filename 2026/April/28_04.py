# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

# You are given a 2D integer grid of size m x n and an integer x. In one operation,
# you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not
# possible, return -1.

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        arr.sort()

        common = arr[len(arr)//2]
        res = 0
        for i in range(len(arr)//2):
            diff = common - arr[i]
            if diff % x:
                return -1
            res += diff // x

        for i in range(len(arr)//2 + 1, len(arr)):
            diff = arr[i] - common
            if diff % x:
                return -1
            res += diff // x

        return res

# <Medium> Topics: Array, Math, Sorting, Matrix
# Runtime 143ms 74.66%
# Memory 40.87MB 76.71%
