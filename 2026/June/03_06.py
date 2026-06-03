#https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii

# You are given two categories of theme park attractions: land rides and water rides.

# landStartTime[i] – the earliest time the ith land ride can be boarded.
# landDuration[i] – how long the ith land ride lasts.

# waterStartTime[j] – the earliest time the jth water ride can be boarded.
# waterDuration[j] – how long the jth water ride lasts.

# A tourist must experience exactly one ride from each category, in either order.

# A ride may be started at its opening time or any later moment.
# If a ride is started at time t, it finishes at time t + duration.
# Immediately after finishing one ride the tourist may board the other (if it
# is already open) or wait until it opens.

# Return the earliest possible time at which the tourist can finish both rides.

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m, n = len(landStartTime), len(waterStartTime)
        minLandEndTime = min([landStartTime[i] + landDuration[i] for i in range(m)])
        minWaterEndTime = min([waterStartTime[i] + waterDuration[i] for i in range(n)])

        landFirst = min([max(minLandEndTime, waterStartTime[i]) + waterDuration[i] for i in range(n)])
        waterFirst = min([max(minWaterEndTime, landStartTime[i]) + landDuration[i] for i in range(m)])

        return min(landFirst, waterFirst)

# <Medium> Array, Two Pointers, Binary Search, Greedy, Sorting
# Runtime 112ms 81.82%
# Memory 34.92MB 43.64%
