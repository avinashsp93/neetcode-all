from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        def dfs(i, combination, remaining):
            if remaining <= 0 or i == len(candidates):
                if remaining == 0:
                    result.append(combination)
                return
            
            # skip branch
            j = i
            while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                j+=1
            dfs(j+1, combination.copy(), remaining)

            # take branch
            remaining -= candidates[i]
            combination.append(candidates[i])
            dfs(i+1, combination.copy(), remaining)

        dfs(0, [], target)
        return result