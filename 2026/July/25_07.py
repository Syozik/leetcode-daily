# https://leetcode.com/problems/maximum-product-of-two-digits

# You are given a positive integer n.
# Return the maximum product of any two digits in n.
# Note: You may use the same digit twice if it appears more than once in n.

class Solution:
    def maxProduct(self, n: int) -> int:
        heap = [0, 0]
        while n:
            digit = n % 10
            n //= 10
            heapq.heappush(heap, digit)
            heapq.heappop(heap)

        return heap[0] * heap[1]

# <Easy> Math, Sorting
# Runtime 0ms 100%
# Memory 19.24MB 54.97%

