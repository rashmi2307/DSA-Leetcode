# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

# Example 1:
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

# Example 2:
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

# Example 3:
# Input: nums = [3,9,6], k = 2
# Output: 1


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        max_freq = 0
        for right in range(len(nums)):
            window_sum +=nums[right]
            cost = nums[right]*(right -left+1) - window_sum
            while cost > k:
                window_sum -=nums[left]
                left+=1
                cost = nums[right]*(right -left+1) - window_sum
            max_freq = max(max_freq,right - left+1)
        return max_freq
    


# - Key Observations

# We can only increment elements, never decrement.
# Therefore, after sorting, we try to make all elements in a window equal to the largest element of that window (nums[right]).
# Sorting is necessary because it groups smaller elements before larger ones.

# - Cost Calculation

# For a window [left...right]:

# Target value = nums[right]
# Window length = right - left + 1
# Operations needed =

# target * window_length - window_sum

# This gives the number of increments required to make every element in the window equal to target.

# - Sliding Window Logic

# Expand the window by moving right.
# If required operations ≤ k, window is valid.
# If required operations > k, shrink from the left until valid again.
# Track the largest valid window size.

# - Why Sliding Window Works

# Array is sorted.
# When cost becomes too large, removing the smallest element (nums[left]) reduces the required operations.
# Both pointers move only forward → efficient O(n) window processing.

# - Pattern Recognition

# If a problem contains:

# "At most k operations"
# "Maximum frequency"
# "Longest/maximum valid subarray"

# Think:

# Sort + Sliding Window

# - One-Line Trick

# > Sort the array, treat the rightmost element as the target, calculate how many increments are needed to bring the whole window up to that target, and shrink the window whenever the cost exceeds k.