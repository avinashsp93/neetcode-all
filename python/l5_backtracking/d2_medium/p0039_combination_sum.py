class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, combination):
            if sum(combination) >= target:
                if sum(combination) == target:
                    result.append(combination)
                return
            dfs(i, combination.copy())
            combination.append(candidates[i])
            dfs(i+1, combination)
        dfs(0, [])