class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        lsum = 0
        rsum = total - nums[0]
        pivot = 0

        while(pivot + 1 < len(nums) and lsum != rsum):
            lsum += nums[pivot]
            rsum -= nums[pivot+1]
            pivot += 1
        if lsum != rsum:
            return -1
        return pivot
        
        