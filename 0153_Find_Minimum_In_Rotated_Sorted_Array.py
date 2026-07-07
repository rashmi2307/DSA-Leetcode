# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.



# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array to find the minimum element.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float("inf")
        for i in range (n):
            if nums[i] < mini:
                mini = nums[i]
        return mini
    



# Binary Search Approach:
# Time Complexity: O(log n) - We are using binary search to find the minimum element
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:

            mid = start + (end - start)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid 

        return nums[start]

