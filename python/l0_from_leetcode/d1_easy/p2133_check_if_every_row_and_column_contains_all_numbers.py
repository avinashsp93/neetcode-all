from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(0, n):
            uniqueElementsRowWise = set()
            uniqueElementsColumnWise = set()
            for j in range(0, n):
                if matrix[i][j] not in uniqueElementsRowWise:
                    uniqueElementsRowWise.add(matrix[i][j])
                else:
                    return False
                
                if matrix[j][i] not in uniqueElementsColumnWise:
                    uniqueElementsColumnWise.add(matrix[j][i])
                else:
                    return False

        return True