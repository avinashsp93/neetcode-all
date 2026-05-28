class Solution:
    def findTheDifference_hashMapApproach(self, s: str, t: str) -> str:
        hashMapT = dict()

        for j in t:
            hashMapT[j] = hashMapT.get(j, 0) + 1

        for i in s:
            hashMapT[i] -= 1

        for k, v in hashMapT.items():
            if v > 0:
                return k
        return ""

    def findTheDifference_xorApproach(self, s: str, t: str) -> str:
        xorResult = 0
        for i in s:
            xorResult ^= ord(i)
        for j in t:
            xorResult ^= ord(j)

        return chr(xorResult)