# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.



# Time Complexity: O(n) - We are iterating through the entire array to find the peak element.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (n):
            left = (i == 0) or (nums[i] >= nums[i-1])
            right = (i == n - 1) or (nums[i] >= nums[i+1])
            if left and right:
                return i
        return -1
    


# Time Complexity: O(log n) - We are using binary search to find the peak element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low