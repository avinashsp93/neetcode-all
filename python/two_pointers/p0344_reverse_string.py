from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)//2):
            j = len(s) - i - 1 # last index
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        