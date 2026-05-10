# https://leetcode.com/problems/cyclically-rotating-a-grid

# You are given an m x n integer matrix grid, where m and n are both even integers,
# and an integer k.

# The matrix is composed of several layers:
# 1 1 1 1
# 1 2 2 1
# 1 2 2 1
# 1 1 1 1

# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix.
# To cyclically rotate a layer once, each element in the layer will take the place of the
# adjacent element in the counter-clockwise direction.
# Return the matrix after applying k cyclic rotations to it.

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*n for _ in range(m)]

        def get_rotated(layer, idx):
            if idx < n - 2*layer:
                return layer, layer + idx
            if idx < n + m - 4*layer - 1:
                return layer + idx - n + 2*layer + 1, n - 1 - layer
            if idx < 2*n + m - 6*layer - 2:
                return m - 1 - layer, layer + 2*n + m - 6*layer - idx - 3
            return layer + 2*(n-4*layer+m-2) - idx, layer

        for layer in range(min(m, n) // 2):
            l = 2*(n-4*layer + m - 2)
            for i in range(n - 2*layer):
                x, y = get_rotated(layer, (i + k) % l)
                res[layer][layer + i] = grid[x][y]

                idx2 = l//2 + n - 2*layer - i - 1
                x, y = get_rotated(layer, (idx2 + k) % l)
                res[m - 1 - layer][layer + i] = grid[x][y]

            for j in range(1, m - 2*layer - 1):
                x, y = get_rotated(layer, (l - j + k) % l)
                res[layer + j][layer] = grid[x][y]

                idx2 = n - 2*layer + j - 1
                x, y = get_rotated(layer, (idx2 + k) % l)
                res[layer + j][n - 1 - layer] = grid[x][y]
        

        return res

# <Medium> Array, Matrix, Simulation
# Runtime 125ms 20.55%
# Memory 19.80MB 4.11%
