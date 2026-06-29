# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^4) where n is the length of the input array
from git import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(nums)
        for i in range (n):
            for j in range (i+1, n):
                for k in range (j+1 ,n):
                    for l in range (k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            triplet = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))     
                            answer.add(triplet)   
        return [list(triplet) for triplet in answer]
    


# Better Approach
# Time Complexity: O(n^3 * log (no. of unique quadruplets)) where n is the length of the input array
# Space Complexity: O(n)+O(2*no. of unique quadruplets) as we are using a set to store the result
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(nums)
        for i in range (n):
            for j in range (i+1, n):
                seen = set()
                for k in range (j+1 ,n):
                    fourth = target - (nums[i] + nums[j]+ nums[k])
                    if fourth in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        answer.add(quad)
                    seen.add(nums[k])
        return [list(quad) for quad in answer]
    




# Optimal Approach
# Time Complexity: O(n^3) where n is the length of the input array
# Space Complexity: O(1) as we are not using any extra space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(nums)
        nums.sort()
        for i in range (n):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            for j in range (i+1, n):
                if j> i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
    
                    if total == target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return answer




