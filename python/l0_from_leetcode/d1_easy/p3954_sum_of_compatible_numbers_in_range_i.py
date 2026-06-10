class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        result = 0
        start = max(0, n-k)
        for x in range(start, n+k+1):
            if n & x == 0:
                result += x
        return result