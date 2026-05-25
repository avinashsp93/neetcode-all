from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(0, n):
            for j in range(0, n):
                if((i == j or i + j == n - 1) and grid[i][j] == 0):
                    return False
                elif((not (i == j or i + j == n - 1)) and grid[i][j] != 0):
                    return False
        return True