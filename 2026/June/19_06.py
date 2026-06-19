# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19

# There is a biker going on a road trip. The road trip consists of n + 1 points at
# different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in
# altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, curr = 0, 0
        for g in gain:
            curr += g
            ans = max(ans, curr)
        return ans

# <Easy> Array, Prefix sum
# Runtime 0ms 100%
# Memory 19.14MB 85.71%
