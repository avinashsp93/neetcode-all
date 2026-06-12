from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,len(matrix)-1
        floorRow = -1
        verticalMid = 0
        while(i <= j):
            verticalMid = (i + j)//2
            if(matrix[verticalMid][0] > target):
                j = verticalMid-1
            elif(matrix[verticalMid][0] < target):
                floorRow = verticalMid
                i = verticalMid+1
            else:
                return True

        k,l = 0,len(matrix[floorRow])-1
        horizontalMid = 0
        while(k <= l):
            horizontalMid = (k + l)//2
            if(matrix[floorRow][horizontalMid] > target):
                l = horizontalMid-1
            elif(matrix[floorRow][horizontalMid] < target):
                k = horizontalMid+1
            else:
                return True

        return False
    
    # Just a problem that gives the idea
    def searchBinary(self, nums, target):
        i,j = 0, len(nums)-1
        ans = -1
        while(i <= j):
            mid = (i + j)//2
            if(nums[mid] > target):
                j = mid - 1
            elif(nums[mid] < target):
                ans = nums[mid] # answer will be the floor of the target
                i = mid + 1
            else:
                print(nums[mid])
                return True
        print("Floor =", ans)
        return False