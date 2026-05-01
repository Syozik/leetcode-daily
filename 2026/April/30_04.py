# https://leetcode.com/problems/maximum-path-score-in-a-grid

# You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

# You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

# Each cell contributes a specific score and incurs an associated cost, according to their cell values:

# 0: adds 0 to your score and costs 0.
# 1: adds 1 to your score and costs 1.
# 2: adds 2 to your score and costs 1.
# Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append([-1]*(k+1))
            dp.append(row)
        dp[0][0][0] = 0
        value_map = {0: (0, 0), 1: (1, 1), 2: (2, 1)}
        for i in range(1, n):
            score, cost = value_map[grid[0][i]]
            for poss_cost in range(k+1):
                if poss_cost + cost <= k:
                    if dp[0][i-1][poss_cost] != -1:
                        dp[0][i][cost + poss_cost] = dp[0][i-1][poss_cost] + score
                else:
                    break

        for i in range(1, m):
            score, cost = value_map[grid[i][0]]
            for poss_cost in range(k+1):
                if poss_cost + cost <= k:
                    if dp[i-1][0][poss_cost] != -1:
                        dp[i][0][cost + poss_cost] = dp[i-1][0][poss_cost] + score
                else:
                    break
    
        for i in range(1, m):
            for j in range(1, n):
                score, cost = value_map[grid[i][j]]
                for poss_cost in range(k+1):
                    if poss_cost + cost <= k:
                        l = max(dp[i][j-1][poss_cost], dp[i-1][j][poss_cost])
                        if l != -1:
                            dp[i][j][cost + poss_cost] = score + l
                    else:
                        break

        return max(dp[-1][-1])

# <Medium> Topics: 
# Runtime 7928ms 57.65%
# Memory 37.41MB 59.69%
