# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation

# You are given an integer array nums of length n.
# You start at index 0, and your goal is to reach index n - 1.

# From any index i, you may perform one of the following operations:
# - Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# - Prime Teleportation: If nums[i] is a prime number p, you may instantly jump
# to any index j != i such that nums[j] % p == 0.

# Return the minimum number of jumps required to reach index n - 1.

class Solution:
    def is_prime(self, num):
        if num <= 1:
            return False
        if not num % 2:
            return num == 2
        for i in range(3, int(sqrt(num)) + 1, 2):
            if not num % i:
                return False
        return True

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        nums_map, primes, max_value = defaultdict(list), set([]), nums[0]
        for i in range(n):
            nums_map[nums[i]].append(i)
            max_value = max(max_value, nums[i])
            if self.is_prime(nums[i]):
                primes.add(nums[i])
    
        visited, queue, jumps = set([-1]), deque([0]), 0

        def add_index(idx):
            if idx not in visited:
                queue.append(idx)
                visited.add(idx)
    
        while queue:
            l = len(queue)
            for _ in range(l):
                idx = queue.popleft()
                if idx == n - 1:
                    return jumps

                add_index(idx-1)
                add_index(idx+1)

                p = nums[idx]
                if p not in primes:
                    continue

                primes.remove(p)
                for k in range(1, max_value//p + 1):
                    for i in nums_map[k*p]:
                        add_index(i)

            jumps += 1

        return 0

# <Medium> Array, Hash Table, Math, BFS, Number Theory
# Runtime 3353ms 57.86%
# Memory 190.23MB 11.63%
