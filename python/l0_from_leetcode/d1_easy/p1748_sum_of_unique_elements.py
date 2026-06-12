from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        elemDict = dict()
        for i in nums:
            elemDict[i] = elemDict.get(i, 0) + 1
        
        uniqueSum = 0
        for k,v in elemDict.items():
            if v == 1:
                uniqueSum += k
        return uniqueSum