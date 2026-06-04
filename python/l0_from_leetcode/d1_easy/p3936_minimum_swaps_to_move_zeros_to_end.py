class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        numLen = len(nums)
        numZeroes = nums.count(0)
        arrayOfInterest = nums[numLen - 1: numLen - 1 - numZeroes: -1]
        return sum(x != 0 for x in arrayOfInterest)