class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            j = 0
            k = i
            while(k < len(haystack) and needle[j] == haystack[k]):
                j+=1
                k+=1
                if j == len(needle):
                    return k - j
        return -1