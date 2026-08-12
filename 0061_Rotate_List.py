# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        for _ in range (k):
            curr = head
            prev = None

            while curr.next:
                prev = curr
                curr = curr.next
            
            prev.next = None
            curr.next = head
            head = curr

        return head





class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head

        k = k % length

        stepsToNewTail = length - k
        newTail = head
        for _ in range (stepsToNewTail - 1):
            newTail = newTail.next

        newHead = newTail.next

        newTail.next = None

        return newHead


