class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        evenNumsMap = dict()
        for i in nums:
            if i%2 == 0:
                evenNumsMap[i] = evenNumsMap.get(i, 0) + 1
        
        for i in range(0, len(nums)):
            if(nums[i]%2 == 0 and evenNumsMap[nums[i]] == 1):
                return nums[i]
        
        return -1