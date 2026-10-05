class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = dict()
        for char in s:
            charDict[char] = charDict.get(char, 0) + 1

        isOddOccurence = False
        count = 0
        for char, occurence in charDict.items():
            if occurence % 2 != 0:
                isOddOccurence = True
                count += occurence - 1
            else:
                count += occurence
        if isOddOccurence:
            count += 1
        return count