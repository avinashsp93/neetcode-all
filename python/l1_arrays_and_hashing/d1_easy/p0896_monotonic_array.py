class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        inc, dec = False, False
        for i in range(0, len(nums)-1):
            if(nums[i+1] - nums[i] > 0):
                inc = True
            elif(nums[i+1] - nums[i] < 0):
                dec = True
        return not inc or not dec