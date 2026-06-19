class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0
        for i in str(n):
            digitSum += int(i)
        
        for j in str(n):
            squareSum += int(j) * int(j)
        
        return True if (squareSum - digitSum) >= 50 else False