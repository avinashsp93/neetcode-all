from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        for i in range(0, len(nums)):
            if target - nums[i] not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [my_dict[target - nums[i]], i]
        return []
