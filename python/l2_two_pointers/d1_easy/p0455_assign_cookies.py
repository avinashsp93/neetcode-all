class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i,j = 0,0

        maxCount = 0
        while(i < len(g) and j < len(s)):
            if(g[i] <= s[j]):
                maxCount += 1
                i+=1
            j+=1
        return maxCount