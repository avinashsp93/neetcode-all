class Solution:
    def check(self, nums: List[int]) -> bool:
        negDiffCount = 0
        for i in range(-1, len(nums)-1):
            if(nums[i+1] - nums[i] < 0):
                negDiffCount += 1
        return negDiffCount <= 1