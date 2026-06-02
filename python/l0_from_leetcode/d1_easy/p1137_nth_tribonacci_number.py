class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def triboAdd(num: int):
            if num not in memo:
                memo[num] = triboAdd(num-1) + triboAdd(num-2) + triboAdd(num-3)
            return memo[num]
        
        return triboAdd(n)