class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(x) != str(n)[0] and str(x) in str(n)[1:]
