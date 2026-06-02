class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def climbStairsRecursive(num):
            if num not in memo:
                memo[num] = climbStairsRecursive(num-1) + climbStairsRecursive(num-2)
            return memo[num]
                
        return climbStairsRecursive(n)