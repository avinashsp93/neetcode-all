from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, right, bottom, left = 0, len(matrix[0])-1, len(matrix)-1, 0
        counter = len(matrix[0]) * len(matrix)
        result = []
        while(top <= bottom and left <= right):
            for i in range(left, right+1):
                result.append(matrix[top][i])
                counter-=1
            top+=1

            if(counter <= 0):
                break

            for j in range(top, bottom+1):
                result.append(matrix[j][right])
                counter-=1
            right-=1

            if(counter <= 0):
                break

            for k in range(right,left-1,-1):
                result.append(matrix[bottom][k])
                counter-=1
            bottom-=1

            if(counter <= 0):
                break

            for l in range(bottom, top-1,-1):
                result.append(matrix[l][left])
                counter-=1
            left+=1

            if(counter <= 0):
                break
        return result