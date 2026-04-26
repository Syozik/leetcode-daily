# https://leetcode.com/problems/detect-cycles-in-2d-grid

# Given a 2D array of characters grid of size m x n, you need to find if there
# exists any cycle consisting of the same value in grid.

# Also, you cannot move to the cell that you visited in your last move. For example, 
# the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited
# (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(x, y, prev):
            if visited[x][y]:
                return True
            visited[x][y] = True
            for i, j in (-1, 0), (1, 0), (0, 1), (0, -1):
                if 0 <= x + i < m and 0 <= y + j < n and (x+i, y+j) != prev and grid[x+i][y+j] == grid[x][y]:
                    if dfs(x+i, y+j, (x, y)):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, (-1, -1)):
                        return True
        
        return False

# <Medium> Topics: Array, DFS, BFS, Union-Find, Matrix
# Runtime 388ms 59.84%
# Memory 86.96MB 65.71%

