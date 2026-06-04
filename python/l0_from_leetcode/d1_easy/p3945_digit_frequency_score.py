class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digitCount = dict()
        
        for i in str(n):
            if i != 0:
                digitCount[i] = digitCount.get(i, 0) + 1
        
        result = 0
        for k,v in digitCount.items():
            result += int(k) * v
        
        return result