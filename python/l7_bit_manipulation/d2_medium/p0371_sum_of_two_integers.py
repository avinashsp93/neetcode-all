class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum, carry = 0,1
        while(carry != 0):
            sum = (a ^ b) & 0xffffffff
            carry = ((a & b) << 1) & 0xffffffff
            a = sum
            b = carry
        return sum