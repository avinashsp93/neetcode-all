from typing import List

class Solution:
    def majorityElement_onePass(self, nums: List[int]) -> int:
        count, result = 0, 0
        for i in nums:
            if(count == 0):
                result = i
            if(result == i):
                count+=1
            else:
                count-=1
        return result

    def majorityElement_trivial(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        max, max_k = 0, 0
        for k,v in my_dict.items():
            if v > max:
                max = v
                max_k = k
        return max_k