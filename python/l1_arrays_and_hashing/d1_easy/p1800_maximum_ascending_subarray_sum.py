class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxAscSum,ascSum = nums[0], nums[0]
        for i in range(0, len(nums)-1):
            if(nums[i] < nums[i+1]):
                ascSum += nums[i+1]
            else:
                ascSum = nums[i+1]
            maxAscSum = max(maxAscSum, ascSum)
        return maxAscSum
