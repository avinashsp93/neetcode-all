class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        i, j = 0, 0
        while(i < len(t) and j < len(s)):
            if(t[i] == s[j]):
                j+=1
            i+=1
        
        return j == len(s)