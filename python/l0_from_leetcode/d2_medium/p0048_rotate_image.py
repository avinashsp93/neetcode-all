from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Intuition : rotate right = flip along diagonal + reverse horizontally

        # since it's a square matrix
        n = len(matrix)

        # flip along diagonal
        for i in range(0, n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(0, n):
            for j in range(0, n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp
        
        return matrix