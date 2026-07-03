# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using dynamic programming technique.
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxp = float("-inf")
        for i in range (n):
            product = 1
            for j in range (i, n):
                product *= nums[j]
                if product > maxp:
                    maxp = product
        return maxp