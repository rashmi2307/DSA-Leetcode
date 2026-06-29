# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.




# Brute Force Approach : Time Limit Exceeded
# Time Complexity: O(n^3) where n is the length of the input array
# Space Complexity: O(n) as we are using a set to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        st = set()
        for i in range (n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                        st.add(triplet)
        return [list(triplet) for triplet in st]
    


# Better Approach
# Time Complexity: O(n^2 * log (no. of unique triplets)) where n is the length of the input array
# Space Complexity: O(n)+O(2*no. of unique triplets) as we are using a set to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = set()
        for i in range (n):
            seen = set()
            for j in range (i+1,n):
                third = -(nums[i]+nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i],nums[j],third]))
                    answer.add(triplet)
                seen.add(nums[j])
        return [list (t) for t in answer]



# Optimal Solution: Use Hashnet and 2 pointers to find the triplets that sum up to 0. Sort the array and use a for loop to iterate through the array. For each element, use two pointers to find the other two elements that sum up to 0. Skip duplicates to avoid duplicate triplets in the answer.    
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(n) as we are using a list to store the result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = []
        nums.sort()
        for i in range (n):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right =  n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return answer