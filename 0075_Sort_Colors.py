# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]



# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        count0, count1, count2 = 0,0,0
        for i in range (n):
            if nums[i] == 0:
                count0 +=1
            if nums[i] == 1:
                count1 +=1
            if nums[i] == 2:
                count2 +=1
        for i in range (count0):
            nums[i] = 0
        for i in range (count0, count0+count1):
            nums[i] = 1
        for i in range (count0+count1, n):
            nums[i] = 2
            
