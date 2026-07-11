# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.





# Brute Force Approach:
# Time Complexity: O(n * m) - We are iterating through the entire array for each possible maximum sum, where m is the sum of the array.
# Space Complexity: O(1) - We are not using any extra space.
class SubarrayPartitioner:
    # Counts how many partitions are needed given maxSum
    def count_partitions(self, a, max_sum):
        partitions = 1  # at least one partition
        subarray_sum = 0  # current subarray sum

        for num in a:
            # Add to current subarray if it doesn't exceed max_sum
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                # Start a new subarray
                partitions += 1
                subarray_sum = num
        return partitions

    # Finds the smallest possible largest subarray sum for exactly k partitions
    def largest_subarray_sum_minimized(self, a, k):
        low = max(a)  # minimum possible max sum
        high = sum(a)  # maximum possible max sum

        # Brute-force check
        for max_sum in range(low, high + 1):
            if self.count_partitions(a, max_sum) == k:
                return max_sum
        return low  # fallback




# Optimized Approach:
# Time Complexity: O(n log m) - We are using binary search to find the minimum largest sum of the split. The binary search will take log m time, where m is the sum of the array. For each mid value, we are iterating through the entire array to count the number of partitions, which will take O(n) time.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low)//2 
            partitions = self.countPartitions(nums, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countPartitions(self,nums, max_sum):
        partitions = 1
        subarray_sum = 0
        for num in nums:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions
    