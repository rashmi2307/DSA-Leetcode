# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



# Brute Force Approach
# Time Complexity: O(n^3) where n is the length of the input array  
# Space Complexity: O(1) as we are using only constant space to store the maximum sum
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        for i in range (n) :
            for j in range (i, n):
                sum = 0
                for k in range (i, j+1):
                    sum += nums[k]
                    maxi = max(sum, maxi)
        return maxi


# Better Approach
# Time Complexity: O(n^2) where n is the length of the input array  
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        for i in range (n) :
            sum = 0
            for j in range (i, n):
                sum += nums[j]
                maxi = max(sum, maxi)
        return maxi
    


# Optimal Approach  : Kadane's Algorithm
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        sum = 0
        for i in range (len(nums)) :
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum <0:
                sum = 0
        return maxi