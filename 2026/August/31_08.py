# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous
# node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous
# node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and
# a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance]
# where minDistance is the minimum distance between any two distinct critical points and
# maxDistance is the maximum distance between any two distinct critical points. If there are
# fewer than two critical points, return [-1, -1].

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_d, first, last = float("inf"), None, None
        idx = 1
        prev = head.val
        head = head.next
        while head and head.next:
            if (head.val < prev and head.val < head.next.val) or (head.val > prev and head.val > head.next.val):
                if last:
                    min_d = min(min_d, idx - last)
                if not first:
                    first = idx
                last = idx
            prev = head.val
            head = head.next
            idx += 1
        if first and last and last != first:
            return min_d, last - first
        return -1, -1

# <Medium> Linked List
# Runtime 64ms 92.19%
# Memory 62.95MB 77.08%
