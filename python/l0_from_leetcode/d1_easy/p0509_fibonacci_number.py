class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        def fiboAdd(num: int):
            if num not in memo:
                memo[num] = fiboAdd(num-1) + fiboAdd(num-2)
            return memo[num]
        
        return fiboAdd(n)