# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

# Example 1:
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

# Example 2:
# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.





from git import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            row = self.row_search(mat, mid)

            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < n else float('-inf')

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return [-1,-1]
    
    def row_search(self, mat, col):
        index = -1
        max_val = float('-inf')

        for i in range (len(mat)):
            if mat[i][col] > max_val:
                max_val = mat[i][col]
                index = i
        return index