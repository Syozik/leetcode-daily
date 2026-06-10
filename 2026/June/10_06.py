# https://leetcode.com/problems/maximum-total-subarray-value-ii

# You are given an integer array nums of length n and an integer k.

# You must select exactly k distinct subarrays nums[l..r] of nums. Subarrays may
# overlap, but the exact same subarray (same l and r) cannot be chosen more than once.

# The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

# The total value is the sum of the values of all chosen subarrays.

# Return the maximum possible total value you can achieve.

class SegmentTrees:
    def __init__(self, els):
        self.els = els
        self.n = len(els)
        self.min = [None] * 4*self.n
        self.max = [None] * 4*self.n
        self.build(1, 0, self.n - 1)

    def build(self, idx, x, y):
        if x == y:
            self.min[idx] = self.els[x]
            self.max[idx] = self.els[x]
            return

        m = (x+y) // 2
        self.build(2*idx, x, m)
        self.build(2*idx+1, m+1, y)
        self.min[idx] = min(self.min[2*idx], self.min[2*idx + 1])
        self.max[idx] = max(self.max[2*idx], self.max[2*idx + 1])

    def query(self, idx, x, y, qx, qy):
        if qx <= x and y <= qy:
            return self.min[idx], self.max[idx]

        if y < qx or x > qy:
            return float("inf"), float("-inf")

        m = (x + y)//2
        left = self.query(2*idx, x, m, qx, qy)
        right = self.query(2*idx + 1, m+1, y, qx, qy)

        return min(left[0], right[0]), max(left[1], right[1])

    def diff(self, left, right):
        if left >= right:
            return 0
        min_value, max_value = self.query(1, 0, self.n-1, left, right)
        return max_value - min_value

class Solution:
    def maxTotalValue(self, nums, k) -> int:
        trees = SegmentTrees(nums)
        ans = 0
        left, right = 0, len(nums) - 1
        seen = set([(left, right)])
        pq = [(-trees.diff(left, right), left, right)]

        for _ in range(k):
            diff, left, right = heappop(pq)
            ans -= diff
            if (left, right - 1) not in seen:
                heappush(pq, (-trees.diff(left, right-1), left, right-1))
                seen.add((left, right - 1))
            if (left + 1, right) not in seen:
                heappush(pq, (-trees.diff(left + 1, right), left + 1, right))
                seen.add((left + 1, right))

        return ans

# <Hard> Array, Greedy, Segment Tree, Heap
# Runtime 8406ms 31.71%
# Memory 62.99MB 24.39%
