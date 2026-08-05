class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        countZeroes = nums.count(0)

        if countZeroes >= 2:
            return [0] * len(nums)
        elif countZeroes == 1:
            zeroIndex = 0
            for index, num in enumerate(nums):
                if num != 0:
                    prod *= num
                else:
                    zeroIndex = index
            result = [0] * len(nums)
            result[zeroIndex] = prod
            return result
        else:
            for index, num in enumerate(nums):
                prod *= num
            result = []
            for num in nums:
                result.append(prod // num)
            return result