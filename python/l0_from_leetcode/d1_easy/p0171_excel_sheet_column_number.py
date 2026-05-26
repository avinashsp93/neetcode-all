class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        finalSum = 0
        j = 0
        for i in columnTitle[::-1]:
            charFaceValue = (ord(i) - 64) * pow(26, j)
            finalSum += charFaceValue
            j+=1
        return finalSum