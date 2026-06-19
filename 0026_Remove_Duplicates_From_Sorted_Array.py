# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i+1
        while j < len(nums):
            if nums[j] == nums[i]:
                j+=1
            else:
                nums[i+1] = nums[j]
                j+=1
                i+=1
        return i+1
    


# Notes:
# Use two pointers i and j.
# i points to the last unique element, j traverses the array.
# If nums[j] == nums[i], j is a duplicate, so we move j forward.
# If nums[j] != nums[i], we found a new unique element, so we move i forward and copy nums[j] to nums[i].
# Time: O(n), Space: O(1).