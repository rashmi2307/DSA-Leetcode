# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3



# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) as we are using a set to store the unique elements of
from git import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        st = set()
        for i in range (len(nums)):
            st.add(nums[i])
        for it in st:
            if it - 1 not in st:
                count = 1
                x = it
                while x + 1 in st:
                    count +=1
                    x+=1
                if count > longest:
                    longest = count
        return longest