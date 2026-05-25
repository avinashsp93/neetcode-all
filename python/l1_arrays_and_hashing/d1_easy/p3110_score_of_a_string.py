class Solution:
    def scoreOfString(self, s: str) -> int:
        acc = 0
        for i in range(0, len(s) - 1):
            acc += abs(ord(s[i]) - ord(s[i+1]))
        return acc