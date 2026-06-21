# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) as we are using only a constant amount of extra space
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxm = 0
        n = len(nums)
        for i in range (n):
            if nums[i] == 1:
                count+=1
            else:
                count = 0
            if count > maxm:
                maxm = count
        return maxm