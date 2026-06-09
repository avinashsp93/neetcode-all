class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        while n is not 0:
            if n & 3 == 3:
                count+=1
            n = n >> 1
        return True if count == 1 else False