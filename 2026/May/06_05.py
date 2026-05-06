# https://leetcode.com/problems/rotating-the-box

# You are given an m x n matrix of characters boxGrid representing a side-view of
# a box. Each cell of the box is one of the following:

# - A stone '#'
# - A stationary obstacle '*'
# - Empty '.'

# The box is rotated 90 degrees clockwise, causing some of the stones to fall due
# to gravity. Each stone falls down until it lands on an obstacle, another stone,
# or the bottom of the box. Gravity does not affect the obstacles' positions, and
# the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone,
# or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        for i in range(m):
            lastIdx = None
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == ".":
                    if not lastIdx:
                        lastIdx = j
                elif boxGrid[i][j] == "#":
                    if lastIdx:
                        boxGrid[i][lastIdx] = "#"
                        boxGrid[i][j] = "."
                        lastIdx -= 1
                else:
                    lastIdx = None
        res = []
        for i in range(n):
            row = []
            for j in range(m-1, -1, -1):
                row.append(boxGrid[j][i])
            res.append(row)
        return res
    

# <Medium> Array, Two Pointers, Matrix
# Runtime 111ms 75.66%
# Memory 54.37MB 66.13%
