# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 
# Example 1:
# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

# Example 2:
# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1




# Brute Force Approach: Time Limit exceeded for large inputs. We can optimize this using merge sort technique.
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range (n):
            for j in range (i+1,n):
                if nums[i] > 2* nums[j]:
                    count += 1
        return count
    


# Optimized Approach: Using merge sort technique to count the reverse pairs.
# Time Complexity: O(nlogn) where n is the length of the input array
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.sort(nums,0,len(nums)-1)

    def sort(self,nums,low,high) -> int:
        count = 0
        if low>=high:
            return count
        mid = (low+high)//2
        count += self.sort(nums,low, mid)
        count += self.sort(nums,mid+1,high)
        count += self.countPairs(nums,low,mid,high)
        self.merge(nums, low, mid, high)
        return count

    def merge(self,nums,low,mid,high):
        temp = []
        left = low
        right = mid + 1
        while left<=mid and right <=high:
            if nums[left] <=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range (low, high + 1):
            nums[i] = temp[i - low]

    def countPairs (self,nums, low, mid, high)-> int:
        count = 0
        right = mid + 1
        for i in range (low,mid + 1):
            while (right <=high and nums[i]>nums[right]*2):
                right += 1
            count += right - (mid + 1)
        return count