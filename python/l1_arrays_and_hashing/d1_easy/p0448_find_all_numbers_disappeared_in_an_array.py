class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            derivedIndex = abs(i) - 1
            nums[derivedIndex] = -abs(nums[derivedIndex])
        result = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result