from typing import List

class Solution:
    # So many approaches

    # straight forward approach
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for i in nums:
            if i in numSet:
                return i
            else:
                numSet.add(i)
        return 0

    