# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations

# You are given two integer arrays, source and target, both of length n. You are
# also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates
# that you are allowed to swap the elements at index ai and index bi (0-indexed)
# of array source. Note that you can swap elements at a specific pair of indices
# multiple times and in any order.

# The Hamming distance of two arrays of the same length, source and target, is the
# number of positions where the elements are different. Formally, it is the number
# of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

# Return the minimum Hamming distance of source and target after performing any amount
# of swap operations on array source.


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        dsu = DSU(len(source))
        for a, b in allowedSwaps:
            dsu.union(a, b)
        
        freq = defaultdict(lambda: defaultdict(int))
        for i in range(len(source)):
            p = dsu.find(i)
            freq[p][source[i]] += 1

        ans = 0
        for i in range(len(target)):
            p = dsu.find(i)
            if freq[p][target[i]] > 0:
                freq[p][target[i]] -= 1
            else:
                ans += 1
        
        return ans

# <Medium> Topics: Array, DFS, Union-Find
# Runtime 220ms 67.67%
# Memory 54.85MB 82.71%

