# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



# Brute Force Approach
# Time Complexity: O(n^2) where n is the number of rows or columns in the input matrix
# Space Complexity: O(n^2) as we are using an extra matrix of size n
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp = [[0] * n for _ in range(n)]
        for i in range (n):
            for j in range (n):
                temp[j][n-i-1] = matrix[i][j]

        for i in range (n):
            for j in range (n):
                matrix[i][j] = temp[i][j] 
        


# Optimal Approach
# Time Complexity: O(n^2) where n is the number of rows or columns in the input matrix
# Space Complexity: O(1) as we are not using any extra space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range (n):
            for j in range (i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()