# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Example 2:
# Input: heights = [2,4]
# Output: 4




# Brute Force Solution: Time Complexity: O(n^2) and Space Complexity: O(1)
# Time Limit Error for large inputs. We can optimize it using stack data structure.
from ast import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        for i in range (n):
            minHeight = float("inf")
            for  j in range (i,n):
                minHeight = min(minHeight, heights[j])
                width = j - i + 1
                area = width*minHeight

                maxArea = max(maxArea,area)

        return maxArea