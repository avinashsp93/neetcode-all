class Solution:
    def minOperations(self, s: str) -> int:
        misMatchCount = 0
        for i in range(0,len(s)):
            ch = s[i]
            if i % 2 == int(ch):
                misMatchCount+=1
        return min(misMatchCount, len(s) - misMatchCount)