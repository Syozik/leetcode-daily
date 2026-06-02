# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i

# You are given two categories of theme park attractions: land rides and water rides.

# landStartTime[i] – the earliest time the ith land ride can be boarded.
# landDuration[i] – how long the ith land ride lasts.

# waterStartTime[j] – the earliest time the jth water ride can be boarded.
# waterDuration[j] – how long the jth water ride lasts.

# A tourist must experience exactly one ride from each category, in either order.

# A ride may be started at its opening time or any later moment.
# If a ride is started at time t, it finishes at time t + duration.
# Immediately after finishing one ride the tourist may board the other
# (if it is already open) or wait until it opens.

# Return the earliest possible time at which the tourist can finish both rides.

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_time = float("inf")
        for i in range(len(landStartTime)):
            curr_time = landStartTime[i] + landDuration[i]
            if curr_time >= min_time:
                continue
            for j in range(len(waterStartTime)):
                new_time = max(curr_time, waterStartTime[j])
                min_time = min(new_time + waterDuration[j], min_time)

        for i in range(len(waterStartTime)):
            curr_time = waterStartTime[i] + waterDuration[i]
            if curr_time >= min_time:
                continue
            for j in range(len(landStartTime)):
                new_time = max(curr_time, landStartTime[j])
                min_time = min(new_time + landDuration[j], min_time)

        return min_time

# <Easy> 
# Runtime 16ms 55.23%
# Memory 19.31MB 56.98%
