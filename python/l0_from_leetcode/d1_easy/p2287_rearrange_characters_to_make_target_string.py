class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        inputChars = dict()
        targetChars = dict()
        for i in s:
            inputChars[i] = inputChars.get(i, 0) + 1
        
        for j in target:
            targetChars[j] = targetChars.get(j, 0) + 1
        
        minValue = float('inf')
        for k,v in targetChars.items():
            minValue = min(minValue, inputChars.get(k, 0)//v)
        
        return int(minValue)