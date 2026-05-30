from typing import List
import copy

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # rotate by 90 = flip along horizontal axis + flip along principal diagonal
        # rotate by 180 = flip along horizontal axis + flip along horizontal axis
        # rotate by 270 = flip along horizontal axis + flip along anti-principal diagonal
        # order matters for 90 and -90(270)

        n = len(mat)
        matchFoundFor90, matchFoundFor180, matchFoundFor270 = True, True, True

        # flip along horizontal axis
        i,j = 0,0
        for i in range(0, n):
            for j in range(0, n//2):
                temp = mat[j][i]
                mat[j][i] = mat[n-1-j][i]
                mat[n-1-j][0] = temp
        
        
        intermediate = copy.deepcopy(mat)
        # rotate by 180 - flip along vertical axis
        i,j = 0,0
        for i in range(0, n):
            for j in range(0, n//2):
                temp = intermediate[i][j]
                intermediate[i][j] = intermediate[i][n-1-j]
                intermediate[i][n-1-j] = temp

        # Compare - 180
        i,j = 0,0
        for i in range(0, n):
            for j in range(0, n):
                if target[i][j] != intermediate[i][j]:
                    matchFoundFor180 = False
                    break
            if not matchFoundFor180:
                break
        
        intermediate = copy.deepcopy(mat)
        # rotate by -90 - flip along anti-principal diagonal
        i,j = 0,0
        for i in range(0, n):
            for j in range(n-1-i, -1, -1):
                temp = intermediate[i][j]
                intermediate[i][j] = intermediate[n-1-j][n-1-i]
                intermediate[n-1-j][n-1-i] = temp

        # Compare - -90
        i,j = 0,0
        for i in range(0, n):
            for j in range(0, n):
                if target[i][j] != intermediate[i][j]:
                    matchFoundFor270 = False
                    break
            if not matchFoundFor270:
                break

        intermediate = copy.deepcopy(mat)
        # rotate by 90 - flip along principal diagonal
        i,j = 0,0
        for i in range(0, n):
            for j in range(i+1, n):
                temp = intermediate[i][j]
                intermediate[i][j] = intermediate[j][i]
                intermediate[j][i] = temp

        # Compare - 90
        i,j = 0,0
        for i in range(0, n):
            for j in range(0, n):
                if target[i][j] != intermediate[i][j]:
                    matchFoundFor90 = False
                    break
            if not matchFoundFor90:
                break
            
        return matchFoundFor90 or matchFoundFor180 or matchFoundFor270
        


