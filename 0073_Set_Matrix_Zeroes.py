# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]




# Brute Force Approach
# Time Complexity: O(m*n*(m+n)) where m is the number of rows and n is the number of columns in the input matrix
# Space Complexity: O(1) as we are not using any extra space
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 0:
                    for col in range (n):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -1
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -1
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0



# Better Approach
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the input matrix
# Space Complexity: O(m+n) as we are using two extra arrays of size m and n
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row = [0]*m
        col = [0]*n
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range (m):
            for j in range (n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0




# Optimal Approach
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the input matrix
# Space Complexity: O(1) as we are not using any extra space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        for j in range (n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        for i in range (m) :
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range (1, m):
            for j in range (1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range (1,m):
            for j in range (1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_col_zero:
            for i in range (m):
                matrix[i][0] = 0
        if first_row_zero:
            for j in range (n):
                matrix[0][j] = 0
        