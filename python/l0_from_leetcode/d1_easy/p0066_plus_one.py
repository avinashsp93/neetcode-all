from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        carry = 1
        result = []
        for i in digits[::-1]:
            sum = i + carry
            if sum == 10:
                sum = 0
                carry = 1
            else:
                carry = 0
            result.append(sum)
        if carry == 1:
            result.append(carry)
        return result[::-1]
