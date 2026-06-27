# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2



# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the count of subarrays
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range (n):
            sum = 0
            for j in range (i,n):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count
    


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a dictionary to store the prefix sum counts
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSumCount = {}
        prefixSumCount[0] = 1
        prefixSum = 0
        count = 0
        for i in range (n):
            prefixSum += nums[i]
            remove = prefixSum - k
            if remove in prefixSumCount:
                count += prefixSumCount[remove]
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
        return count