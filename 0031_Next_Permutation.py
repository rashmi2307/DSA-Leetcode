# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]



# Brute Force Approach
# Time Complexity: O(n*n!) where n is the length of the input array
# Space Complexity: O(n*n!) as we are storing all the permutations of the input array
from itertools import permutations
class Solution:
    def nextPermutation(self, nums):
        # Your code goes here
        perms = sorted(set(permutations(nums)))
        current = tuple(nums)
        for i in range(len(perms)):
            if perms[i] == current:
                if i == len(perms) - 1:
                    return list(perms[0])
                return list(perms[i+1])
        return nums
    


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the index
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        for i in range (len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums.reverse()
            return
        for i in range (len(nums)-1, index, -1):
            if nums[i] > nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
                break
        nums[index+1:] = reversed(nums[index+1:])











