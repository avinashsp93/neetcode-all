from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subsets = []
        def dfs(i, subset):
            if i == len(nums):
                subsets.append(subset)
                return
            
            # skip branch
            j = i
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j+=1
            dfs(j+1, subset.copy())

            # take branch
            subset.append(nums[i])
            dfs(i+1, subset.copy())
            
        dfs(0, [])
        return subsets