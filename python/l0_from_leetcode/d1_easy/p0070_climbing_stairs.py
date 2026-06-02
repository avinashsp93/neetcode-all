class Solution:
    memo = dict()
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def climbStairsRecursive(n):
            if n not in memo:
                memo[n] = climbStairsRecursive(n-1) + climbStairsRecursive(n-2)
            return memo[n]
                
        return climbStairsRecursive(n)