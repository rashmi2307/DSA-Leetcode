# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]




# Iterative Approach:
# Time Complexity: O(log n) - We are iterating through the entire array to find the first and last occurrence of the target integer.
# Space Complexity: O(1) - We are not using any extra space.
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.getFirst(nums, target)
        last = self.getLast(nums, target)
        return [first, last]

    def getFirst(self,nums,target):
        answer = -1
        low = 0
        high = len(nums) -1
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target:
                answer = mid
                high = mid - 1
            elif nums[mid] < target :
                low = mid + 1
            elif nums[mid] > target :
                high = mid -1
        return answer

    def getLast(self,nums, target):
        answer = -1
        low = 0
        high  = len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid] == target:
                answer = mid
                low = mid + 1
            elif nums[mid] < target :
                low = mid + 1
            elif nums[mid] > target :
                high = mid -1
        return answer