from typing import List

class Solution:
    def singleNonDuplicate_BigO_N(self, nums: List[int]) -> int:
        my_set = set()
        for i in nums:
            if i in my_set:
                my_set.remove(i)
            else:
                my_set.add(i)
        return my_set.pop()

    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while(low <= high):
            mid = (low + high)//2
            isEvenMid = mid % 2 == 0

            leftSame = mid > 0 and nums[mid] == nums[mid-1]
            rightSame = mid < len(nums)-1 and nums[mid] == nums[mid+1]

            if not leftSame and not rightSame:
                return nums[mid]

            if isEvenMid:
                if rightSame:
                    low = mid + 2
                else:
                    high = mid - 2
            else:
                if leftSame:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1