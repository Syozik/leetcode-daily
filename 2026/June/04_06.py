# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i

# You are given two integers num1 and num2 representing an inclusive range [num1, num2].

# The waviness of a number is defined as the total count of its peaks and valleys:

# A digit is a peak if it is strictly greater than both of its immediate neighbors.
# A digit is a valley if it is strictly less than both of its immediate neighbors.
# The first and last digits of a number cannot be peaks or valleys.

# Any number with fewer than 3 digits has a waviness of 0.

# Return the total sum of waviness for all numbers in the range [num1, num2].

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(n: str) -> int:
            ans = 0
            for i in range(1, len(n) - 1):
                if n[i-1] < n[i] and n[i] > n[i+1]:
                    ans += 1
                elif n[i-1] > n[i] and n[i] < n[i+1]:
                    ans += 1
            return ans
        
        ans = 0
        for i in range(max(100, num1), num2+1):
            ans += get_waviness(str(i))

        return ans

# <Medium> Math, DP, Enumeration
# Runtime 247ms 82.76%
# Memory 19.23MB 69.73%
