from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(string) for string in strs])
        acc = ""
        for i in range(0, min_length):
            charAtI = strs[0][i]
            for string in strs:
                if(string[i] != charAtI):
                    return acc
            acc+= charAtI
        return acc