from typing import List

class Solution:
    # Solution using dictionary
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = dict()
        for i in range(0, len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = i
            else:
                return True
        return False
    
    # Alternative solution using set
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))