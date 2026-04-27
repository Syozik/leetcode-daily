# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid

# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.

# You will initially start at the street of the upper-left cell (0, 0). A valid path
# in the grid is a path that starts from the upper left cell (0, 0) and ends at the
# bottom-right cell (m - 1, n - 1). The path should only follow the streets.

# Return true if there is a valid path in the grid or false otherwise.

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        roads = {
            1: ((0, -1), (0, 1)),
            2: ((-1, 0), (1, 0)),
            3: ((0, -1), (1, 0)),
            4: ((1, 0), (0, 1)),
            5: ((-1, 0), (0, -1)),
            6: ((-1, 0), (0, 1))
        }
        def dfs(x, y):
            if (x, y) == (m-1, n-1):
                return True
            road = grid[x][y]
            if not road:
                return False
            # mark it as visited
            grid[x][y] = 0
            for i, j in roads[road]:
                # if out of bounds or already visited
                if not (0 <= x + i < m and 0 <= y + j < n and grid[x+i][y+j]):
                    continue
                next_road = grid[x+i][y+j]
                for i2, j2 in roads[next_road]:
                    # it means the roads are connected
                    if (i, j) == (-i2, -j2):
                        if dfs(x+i, y+j):
                            return True
            return False
    
        return dfs(0, 0)

# <Medium> Topics: Array, DFS, BFS, Union-Find, Matrix
# Runtime 240ms 34.70%
# Memory 58.74MB 29.11%

