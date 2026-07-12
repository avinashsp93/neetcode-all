class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(i, subset):
            if i == len(nums):
                subsets.append(subset)
                return
            dfs(i+1, subset.copy())
            subset.append(nums[i])
            dfs(i+1, subset)
        dfs(0, [])
        return subsets