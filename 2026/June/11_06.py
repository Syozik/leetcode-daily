# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i

# There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1.
# The tree is represented by a 2D integer array edges of length n - 1, where
# edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

# Initially, all edges have a weight of 0. You must assign each edge a weight of
# either 1 or 2.
# The cost of a path between any two nodes u and v is the total weight of all edges
# in the path connecting them.

# Select any one node x at the maximum depth. Return the number of ways to assign edge
# weights in the path from node 1 to x such that its total cost is odd.
# Since the answer may be large, return it modulo 10^9 + 7.

# Note: Ignore all edges not in the path from node 1 to x.


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        root = set(range(n))
        for u, v in edges:
            graph[u-1].append(v-1)
            if v - 1 in root:
                root.remove(v-1)
        root = list(root)[0]

        def get_depth(node):
            res = 0
            for child in graph[node]:
                res = max(1 + get_depth(child), res)
            return res

        length = get_depth(root)
        return (2**(length - 1) % (10**9 + 7))

# <Medium> Math, Tree, DFS
# Runtime 351ms 69.89%
# Memory 104.75MB 38.71%
