class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        identicalPairCount = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    identicalPairCount+=1
        return identicalPairCount