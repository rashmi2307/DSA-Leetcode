# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



# Brute Force Approach:
# Time Complexity: O(m+n) - We are merging two sorted arrays into one sorted array
# Space Complexity: O(m+n) - We are using extra space to store the merged array.
from ast import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        final = []
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1

        while i < m:
            final.append(nums1[i])
            i += 1

        while j < n:
            final.append(nums2[j])
            j += 1

        k = len(final)

        if k == 1:
            return final[0]
            
        if k % 2 == 0:
            return (final[k//2] + final[k//2-1])/2
        else:
            return final[k//2]
        



    
# Optimized Approach:
# Time Complexity: O(log(min(m,n))) - We are performing binary search on the smaller array to find the correct partition. The binary search will take log(min(m,n)) time, where m and n are the sizes of the two arrays.
# Space Complexity: O(1) - We are not using any extra space.


