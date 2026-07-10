class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairSet = set()
        for i in nums:
            if i in pairSet:
                pairSet.remove(i)
            else:
                pairSet.add(i)
        return len(pairSet) == 0