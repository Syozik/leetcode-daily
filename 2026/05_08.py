# https://leetcode.com/problems/remove-methods-from-project

# You are maintaining a project that has n methods numbered from 0 to n - 1.

# You are given two integers n and k, and a 2D integer array invocations, where
# invocations[i] = [ai, bi] indicates that method ai invokes method bi.

# There is a known bug in method k. Method k, along with any method invoked by it,
# either directly or indirectly, are considered suspicious and we aim to remove them.

# A group of methods can only be removed if no method outside the group invokes any methods
# within it.

# Return an array containing all the remaining methods after removing all the suspicious
# methods. You may return the answer in any order. If it is not possible to remove all the
# suspicious methods, none should be removed.


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        reversed_graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)
            reversed_graph[b].append(a)

        suspicious = set()
        def dfs(i):
            suspicious.add(i)
            for nei in graph[i]:
                if nei not in suspicious:
                    dfs(nei)
        dfs(k)
        for method in suspicious:
            for nei in reversed_graph[method]:
                if nei not in suspicious:
                    return list(range(n))

        res = []
        for i in range(n):
            if i not in suspicious:
                res.append(i)

        return res

# <Medium> DFS, BFS, Graph Theory
# Runtime 551ms 21.21%
# Memory 127.19MB 40.15%
