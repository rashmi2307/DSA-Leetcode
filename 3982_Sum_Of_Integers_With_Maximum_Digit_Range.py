# You are given an integer array nums.

# The digit range of an integer is defined as the difference between its largest digit and smallest digit.

# For example, the digit range of 5724 is 7 - 2 = 5.

# Return the sum of all integers in nums whose digit range is equal to the maximum digit range among all integers in the array.

# Example 1:
# Input: nums = [5724,111,350]
# Output: 6074
# Explanation:
# i	nums[i]	Largest	Smallest	Digit Range
# 0	5724	7	2	5
# 1	111	1	1	0
# 2	350	5	0	5
# The maximum digit range is 5. The integers with this digit range are 5724 and 350, so the answer is 5724 + 350 = 6074.

# Example 2:
# Input: nums = [90,900]
# Output: 990
# Explanation:
# i	nums[i]	Largest	Smallest	Digit Range
# 0	90	9	0	9
# 1	900	9	0	9
# The maximum digit range is 9. Both integers have this digit range, so the answer is 90 + 900 = 990.



# Time Complexity: O(n * m) - We are iterating through the entire array to find the largest and smallest digit of each integer, where n is the length of the array and m is the number of digits in the integer.
# Space Complexity: O(n) - We are using a dictionary to store the digit range of
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        n = len(nums)
        digit_range = {}

        for i in range (n):
            larg, small = 0, 9

            for j in str(nums[i]):
                if int(j) > int(larg):
                    larg = int(j)
                if int(j) < int(small):
                    small = int(j)
            digit_range[i] = larg - small

        largest_range = 0
        indexes = []

        for i, value in digit_range.items():

            if value > largest_range:
                largest_range = value
                indexes = [i]
            elif value == largest_range:
                indexes.append(i)

        ans = 0
        
        for i in indexes:
            ans = ans + nums[i]
        return ans