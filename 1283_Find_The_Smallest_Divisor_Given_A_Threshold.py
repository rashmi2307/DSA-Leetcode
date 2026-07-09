# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

#  Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

# Example 2:
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44




# Brute Force Approach:
# Time Complexity: O(n * max(nums)) - We are iterating through the entire array
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for divisor in range (1, max(nums)+1):
            sum = 0
            for i in range (len(nums)):
                sum += ceil(nums[i]/divisor)
            if sum <=threshold:
                return divisor
        return -1
    



# Optimized Approach:
# Time Complexity: O(n * log(max(nums))) - We are iterating through the entire array and for each divisor we are checking if it is possible to get the sum less than or equal to threshold.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        if len(nums) > threshold:
            return -1

        low = 1
        high = max(nums) 

        while low <= high:
            mid = (low+high)//2
            if self.sumByD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


    def sumByD(self, nums, divisor):
        return sum(ceil(x/divisor) for x in nums)

