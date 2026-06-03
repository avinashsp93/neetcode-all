from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyDict = dict()
        for i in arr:
            luckyDict[i] = luckyDict.get(i, 0) + 1
        
        largestLucky = -1

        for k,v in luckyDict.items():
            if k == v and k > largestLucky:
                largestLucky = k
        return largestLucky