from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        maxSoFar = 1
        for i in range(0, len(nums)-1):
            if(nums[i] < nums[i+1]):
                inc += 1
                maxSoFar = max(maxSoFar, dec)
                dec = 1
            elif(nums[i] > nums[i+1]):
                dec += 1
                maxSoFar = max(maxSoFar, inc)
                inc = 1
            else:
                maxSoFar = max(inc, dec, maxSoFar)
                inc = 1
                dec = 1
        return max(maxSoFar, inc, dec)
