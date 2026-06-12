from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        originalArray = [pref[0]]
        for i in range(1, len(pref)):
            originalArray.append(pref[i-1] ^ pref[i])
        return originalArray
    
    def findArray_inPlace(self, pref: List[int]) -> List[int]:
        for i in range(len(pref)-1, 0, -1):
            pref[i] = pref[i] ^ pref[i-1]
        return pref