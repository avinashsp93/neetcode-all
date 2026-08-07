class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixSumDict = dict()
        for row in wall:            
            prefixSum = 0
            for brick in row[0:-1:1]:
                prefixSum += brick
                if prefixSum != len(wall):
                    prefixSumDict[prefixSum] = prefixSumDict.get(prefixSum, 0) + 1
        maxVal = 0
        for key, val in prefixSumDict.items():
            if val > maxVal:
                maxVal = val
        return len(wall) - maxVal