from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        unique = set()
        for i in nums:
            unique.add(i)
        runningXor = 0
        for j in unique:
            runningXor ^= j
        for k in nums:
            runningXor ^= k
        return runningXor