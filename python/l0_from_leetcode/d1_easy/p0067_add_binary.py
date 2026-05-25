class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        i = len(a) - 1
        j = len(b) - 1
        sum = 0
        carry = 0
        result = ""
        while(maxLen > 0):
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            if carry == 0:
                sum = bit_a ^ bit_b
                carry = bit_a & bit_b
            else:
                sum = (bit_a ^ bit_b) ^ 1 # bitwise x-nor in python
                carry = bit_a | bit_b
            maxLen-=1
            i-=1
            j-=1
            result+=str(sum)
        if carry == 1:
            result+=str(carry)
        return result[::-1]