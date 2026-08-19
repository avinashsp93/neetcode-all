class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDict = { 0: 1 }
        prefixSum = 0
        result = 0
        for num in nums:
            prefixSum += num
            prefixDict[prefixSum] = prefixDict.get(prefixSum, 0) + 1
            result += prefixDict[prefixSum]
        return result

    def subarraySum_simplerSolution(self, nums: List[int], k: int) -> int:
        prefixDict = { 0: 1 }
        prefixSum = 0
        result = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixDict:
                result += prefixDict[prefixSum - k]
            prefixDict[prefixSum] = prefixDict.get(prefixSum, 0) + 1
        return result