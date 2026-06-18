class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1,x
        while(low <= high):
            mid = (low + high)//2
            sq = mid * mid
            if(sq > x):
                high = mid - 1
            elif(sq < x):
                low = mid + 1
            else:
                return mid
        return high