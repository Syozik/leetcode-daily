# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount

# A shop is selling candies at a discount. For every two candies sold, the shop gives
# a third candy for free.

# The customer can choose any candy to take away for free as long as the cost of the
# chosen candy is less than or equal to the minimum cost of the two candies bought.

# For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys
# candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the
# candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy,
# return the minimum cost of buying all the candies.

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        price = 0
        cost.sort(reverse=True)
        for i in range(0, len(cost), 3):
            price += cost[i]
            if i + 1 < len(cost):
                price += cost[i+1]

        return price

# <Easy> Array, Greedy, Sorting
# Runtime 3ms 27.74%
# Memory 19.45MB 15.37%
