# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

# Example 1:
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

# Example 2:
# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].



# Brute Force Approach
# Time Complexity: O(n) where n is the length of the input array    
# Space Complexity: O(n) as we are using extra space to store the positive and negative numbers
class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        pos = []
        neg = []
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range (n//2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums
    


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using extra space to store the result array
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                result[positive] = nums[i]
                positive += 2
            else:
                result[negative] = nums[i]
                negative += 2
        return result