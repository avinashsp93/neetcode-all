class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        leftRightVisited = set()
        uniqueThreeLengthPalindrome = set()
        for left in range(0,len(s)-2):
            for right in range(len(s)-1,left+1,-1):
                if(s[left] not in leftRightVisited and s[left] == s[right]):
                    leftRightVisited.add(s[left])
                    midVisited = set()
                    pal = ""
                    for mid in range(left+1, right):
                        if(s[mid] not in midVisited):
                            pal = s[left] + s[mid] + s[right]
                            uniqueThreeLengthPalindrome.add(pal)
        return uniqueThreeLengthPalindrome