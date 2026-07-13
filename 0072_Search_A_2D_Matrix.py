# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false



# Brute Force Approach:
# Time Complexity: O(m*n) - We are traversing the entire matrix to find the target element.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for i in range (m):
            for j in range (len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False
                


# Better Approach:
# Time Complexity: O(m+n) - We are traversing the matrix in a linear fashion to find the target element.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        for i in range (n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                return self.binarySearch(matrix[i], target)

        return False
                
    def binarySearch(self, matrix, target):
        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = (low+high)//2

            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                low = mid+1
            else:
                high = mid - 1
        return False





# Optimal Approach:
# Time Complexity: O(log(m*n)) - We are performing binary search on the entire matrix
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low+high)//2

            row = mid // m
            column = mid % m

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False