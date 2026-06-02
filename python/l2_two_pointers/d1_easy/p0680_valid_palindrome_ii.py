class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):
            if(s[left] == s[right]):
                left+=1
                right-=1
            else:
                if(s[left:right] == s[right-len(s)-1:left-len(s)-1:-1]):
                    return True
                elif(s[left+1:right+1] == s[right-len(s):left-len(s):-1]):
                    return True
                return False
        return True