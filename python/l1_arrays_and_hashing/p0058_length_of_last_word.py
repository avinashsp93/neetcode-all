class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        while(s[i] == " "):
            i-=1
        while(i >= 0 and s[i] != " "):
            counter+=1
            i-=1
        return counter