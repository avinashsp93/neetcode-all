class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1
        if dividend == 0:
            return 0
        else:
            if (dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0):
                sign = 1
        calcQuotient = 0
        if sign == -1:
            if dividend < 0:
                while(dividend + divisor <= 0):
                    dividend += divisor
                    calcQuotient += 1
            else:
                while(dividend + divisor >= 0):
                    dividend += divisor
                    calcQuotient += 1
        else:
            if dividend < 0:
                while(dividend - divisor <= 0):
                    dividend -= divisor
                    calcQuotient += 1
            else:
                while(dividend - divisor >= 0):
                    dividend -= divisor
                    calcQuotient += 1
        return calcQuotient if sign == 1 else -calcQuotient
