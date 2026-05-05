# https://leetcode.com/problems/rotate-list

# Given the head of a linked list, rotate the list to the right by k places.

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        copy = head
        tail = head
        l = 0
        while copy:
            copy = copy.next
            l += 1
            if copy:
                tail = copy
        k = k % l
        if not k:
            return head
        end = head
        for i in range(l - k - 1):
            end = end.next 
        new_head = end.next
        end.next = None
        tail.next =  head
        return new_head

# <Medium> Linked List, Two Pointers
# Runtime 0ms 100.0%
# Memory 19.37MB 36.28%
