from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        top, right, bottom, left = 0, n-1, n-1, 0
        counter = 1
        while(counter <= n * n):
            for i in range(left, right+1):
                matrix[top][i] = counter
                counter+=1
            top+=1
            if counter > n * n:
                break

            for j in range(top, bottom+1):
                matrix[j][right] = counter
                counter+=1
            right-=1
            if counter > n * n:
                break


            for k in range(right, left-1, -1):
                matrix[bottom][k] = counter
                counter+=1
            bottom-=1
            if counter > n * n:
                break

            for l in range(bottom, top-1, -1):
                matrix[l][left] = counter
                counter+=1
            left+=1
            if counter > n * n:
                break
        
        return matrix