from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,len(matrix)-1
        verticalMid = 0
        while(i <= j):
            verticalMid = (i + j)//2
            if(matrix[verticalMid][0] > target):
                j = verticalMid-1
            elif(matrix[verticalMid][0] < target):
                if verticalMid+1 < len(matrix) and matrix[verticalMid+1][0] > target:
                    break
                i = verticalMid+1
            else:
                return True

        k,l = 0,len(matrix[verticalMid])-1
        horizontalMid = 0
        while(k <= l):
            horizontalMid = (k + l)//2
            if(matrix[verticalMid][horizontalMid] > target):
                l = horizontalMid-1
            elif(matrix[verticalMid][horizontalMid] < target):
                k = horizontalMid+1
            else:
                return True

        return False