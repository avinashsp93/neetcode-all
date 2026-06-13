class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mostRecentOneIndex = -1
        mostRecentTwoIndex = -1
        minLength = float('inf')
        for index, num in enumerate(nums):
            if(num == 1):
                mostRecentOneIndex = index
                if mostRecentTwoIndex > -1:
                    minLength = min(minLength, mostRecentOneIndex - mostRecentTwoIndex)
            elif(num == 2):
                mostRecentTwoIndex = index
                if mostRecentOneIndex > -1:
                    minLength = min(minLength, mostRecentTwoIndex - mostRecentOneIndex)
        if minLength == float('inf'):
            return -1
        return int(minLength)