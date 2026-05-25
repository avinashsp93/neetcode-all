class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCountInBallonString = dict()
        for i in text:
            charCountInBallonString[i] = charCountInBallonString.get(i, 0) + 1
        minCount = float('inf')
        for j in ['b', 'a', 'l', 'o', 'n']:
            if j in ['l', 'o']:
                minCount = min(minCount, charCountInBallonString.get(j, 0)//2)
            else:
                minCount = min(minCount, charCountInBallonString.get(j, 0)//1)
        return minCount