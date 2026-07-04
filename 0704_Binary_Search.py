# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1



# Iterative Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the target integer.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            mid_value = nums[mid]
            if target == mid_value:
                return mid
            elif target > mid_value:
                low = mid+1
            else:
                high = mid-1
        return -1