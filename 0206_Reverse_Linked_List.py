# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []



# Brute Force approach is to use a stack to store the values of the linked list and then create a new linked list in reverse order. However, this approach uses extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head

        while temp:
            temp.val = stack.pop()
            temp = temp.next
        
        return head




# Optimal approach is to use three pointers to reverse the linked list in place. This approach uses O(1) extra space.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        temp = head

        while temp:
            front = temp.next

            temp.next = prev

            prev = temp

            temp = front

        return prev




