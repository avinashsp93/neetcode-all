class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            
            return dfs(i + 1, total + nums[i+1]) + dfs(i + 1, total)
        
        return(0, 0)