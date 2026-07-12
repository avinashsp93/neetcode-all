from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, combination, remaining):
            if remaining <= 0 or i == len(candidates):
                if remaining == 0:
                    result.append(combination)
                return

            dfs(i+1, combination.copy(), remaining)
            remaining -= candidates[i]
            combination.append(candidates[i])
            dfs(i, combination, remaining)
            

        dfs(0, [], target)
        return result