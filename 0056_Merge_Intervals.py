# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Example 3:
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.



# Brute Force Approach 
# Time Complexity: O(n^2) where n is the length of the input array
from ast import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        n = len(intervals)
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            j = i+1
            while j < n and intervals[j][0] <=end:
                end = max(end,intervals[j][1])
                j += 1
            answer.append([start,end])
            i = j
        return answer