class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        stringOccurences = dict()

        for i in arr:
            stringOccurences[i] = stringOccurences.get(i, 0) + 1
        
        for i in arr:
            if stringOccurences[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""