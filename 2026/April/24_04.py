# https://leetcode.com/problems/furthest-point-from-origin/

# You are given a string moves of length n consisting only of characters 'L',
# 'R', and '_'. The string represents your movement on a number line starting
# from the origin 0.

# In the ith move, you can choose one of the following directions:
# - move to the left if moves[i] = 'L' or moves[i] = '_'
# - move to the right if moves[i] = 'R' or moves[i] = '_'
# Return the distance from the origin of the furthest point you can get to after n moves.

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        possible = {"L": 0, "R": 0, "_": 0}
        for move in moves:
            possible[move] += 1
        left = abs(possible["L"] + possible["_"] - possible["R"])
        right = abs(possible["R"] + possible["_"] - possible["L"])
        return max(left, right)

# <Easy> Topics: String, Counting
# Runtime 0ms 100%
# Memory 19.2MB 84.21%

