# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10




# Time Complexity: O(n) - We are iterating through the entire array to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start = 0
        end = n - 1
        for i in range (n):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[i]
            if i == n-1 and nums[i] != nums[i-1]:
                return nums[i]
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        return -1

 

# Time Complexity: O(n) - We are iterating through the entire array to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range (n):
            answer ^= nums[i]
        return answer
    


# Time Complexity: O(log n) - We are using binary search to find the single element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        low = 1
        high = n - 2

        while low <= high:

            mid = (low+high)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2 == 0 and nums[mid] == nums[mid+1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1