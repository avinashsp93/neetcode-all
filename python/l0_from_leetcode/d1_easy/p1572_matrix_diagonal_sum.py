from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(0, len(mat)):
            j = len(mat) - 1 - i
            if(i != j):
                sum += mat[i][i] + mat[i][j]
            else:
                sum += mat[i][i]
        return sum