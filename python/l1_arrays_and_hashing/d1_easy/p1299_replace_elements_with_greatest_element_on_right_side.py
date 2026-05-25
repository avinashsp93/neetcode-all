from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1 for i in range(0, len(arr))]

        for j in range(len(arr)-2, -1, -1):
            result[j] = max(arr[j+1], result[j+1])
        
        return result

