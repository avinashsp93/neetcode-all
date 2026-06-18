class Solution:
    def arrangeCoins_BigO_N(self, n: int) -> int:
        step = 0
        count = 0
        while(n > 0):
            step += 1
            n -= step
            if(n >= 0):
                count += 1
            else:
                return count
        return count
    
    def arrangeCoins_BigO_LogN(self, n: int) -> int:
        low, high = 1, n
        while(low <= high):
            mid = (low + high)//2
            numCoinsInMid = (mid * (mid + 1))//2
            if(n < numCoinsInMid):
                high = mid - 1
            elif(n > numCoinsInMid):
                low = mid + 1
            else:
                return mid
        return high
    
    def arrangeCoins_BigO_1(self, n: int) -> int:
        return int(((-1 + (1 + 8*n)**0.5)//2))