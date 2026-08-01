from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        inputCharDict = Counter(s)

        result = ""
        for o in order:
            if o in s:
                result += o * inputCharDict[o]

        for k,v in inputCharDict.items():
            if k not in order:
                result += k * v
        return result
