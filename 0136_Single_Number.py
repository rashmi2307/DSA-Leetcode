# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0
        for i in range(len(nums)):
            XOR = XOR ^ nums[i]
        return XOR