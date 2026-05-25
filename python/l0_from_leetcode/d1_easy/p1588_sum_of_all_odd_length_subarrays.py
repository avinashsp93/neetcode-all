from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(0, len(arr)):
            runningSum = 0
            for j in range(i, len(arr)):
                runningSum += arr[j]
                if (i - j) % 2 == 0:
                    result += runningSum
        return result