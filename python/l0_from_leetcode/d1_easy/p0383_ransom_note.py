class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magChars = dict()
        for i in magazine:
            magChars[i] = magChars.get(i, 0) + 1
        
        for j in ransomNote:
            if j in magChars and magChars[j] > 0:
                magChars[j] -= 1
            else:
                return False
        return True
