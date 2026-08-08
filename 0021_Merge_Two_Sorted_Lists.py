# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp1 = list1
        temp2 = list2

        while temp1 is not None:
            arr.append(temp1.val)
            temp1 = temp1.next

        while temp2 is not None:
            arr.append(temp2.val)
            temp2 = temp2.next

        arr.sort()
        head = self.convert_arr_to_linked_list(arr)
        return head

    def convert_arr_to_linked_list(self,arr):
        dummy_node = ListNode(-1)
        temp = dummy_node

        for i in range (len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return dummy_node.next






class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        temp = dummy_node

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummy_node.next
