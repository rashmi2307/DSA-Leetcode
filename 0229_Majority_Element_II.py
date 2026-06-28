# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]



# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the result
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range (n):
            if len(result) == 0 or result[0] != nums[i]:
                count = 0
                for j in range (n):
                    if nums[i] == nums[j]:
                        count+=1
                if count > n//3:
                    result.append(nums[i])
            if len(result) == 2:
                break
        return result
    



# Better Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a dictionary to store the counts of each
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        mini = n // 3 + 1
        mpp = defaultdict(int)
        for num in nums:
            mpp[num] += 1
            if mpp[num] == mini:
                result.append(num)
            if len(result) == 2:
                break
        return result
    




# Optimal Approach : Boyer-Moore Voting Algorithm
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the result
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0,0
        n = len(nums)
        el1, el2 = float("-inf"), float("-inf")
        for num in nums:
            if count1 == 0 and num != el2:
                el1 = num
                count1 = 1
            elif count2 == 0 and num != el1:
                el2 = num
                count2 = 1
            elif num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == el1:
                count1 += 1
            if num == el2:
                count2 += 1
        result = []
        mini = n // 3 + 1
        if count1 >= mini:
            result.append(el1)
        if count2 >= mini and el1 != el2:
            result.append(el2)
        return result