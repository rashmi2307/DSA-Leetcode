# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.



# Brute Force Approach: My Own
# Time Complexity: O(n) - We are iterating through the entire array.
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range (len(arr) + k+1):
            if i not in arr:
                missing.append(i)
            
        return missing[k]





# Brute Force Approach:
# Time Complexity: O(n) - We are iterating through the entire array.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k





