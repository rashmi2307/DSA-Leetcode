# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3



# Brute Force Approach:
from git import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st = set()
        for i in range(len(nums)):
            if nums[i] not in st:
                st.add(nums[i])
            else:
                return nums[i]