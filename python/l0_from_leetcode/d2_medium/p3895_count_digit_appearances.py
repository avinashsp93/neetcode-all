class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for num in nums:
            if num == 0 and digit == 0:
                count+=1
            while(num != 0):
                if num % 10 == digit:
                    count += 1
                num //= 10
        return count