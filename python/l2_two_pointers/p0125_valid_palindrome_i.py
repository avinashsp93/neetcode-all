class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        onlySplChars = True
        for i in s:
            if self.isalphanumeric(i):
                onlySplChars = False

        i = 0
        j = len(s) - 1
        
        if onlySplChars:
            return True
        else:
            while(i < j):
                while(i < j and not self.isalphanumeric(s[i])):
                    i+=1
                while(i < j and not self.isalphanumeric(s[j])):
                    j-=1
                l = s[i]
                r = s[j]
                if(l.lower() != r.lower()):
                    return False
                i+=1
                j-=1
            return True
    
    def isalphanumeric(self, t: str) -> bool:
        ascii_val = ord(t)
        return ((ascii_val >= 65 and ascii_val <= 90) 
                or (ascii_val >= 97 and ascii_val <= 122)
                or (ascii_val >= 48 and ascii_val <= 57))