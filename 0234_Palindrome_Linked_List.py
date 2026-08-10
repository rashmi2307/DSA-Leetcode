# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        temp = head

        while temp is not None:
            st.append(temp.val)
            temp = temp.next
        temp = head

        while temp is not None:
            if temp.val != st[-1]:
                return False
            st.pop()
            temp = temp.next
        return True