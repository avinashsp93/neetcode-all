class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        
        if k == 1:
            return 0
        
        minDif = float('inf')

        left, right = 0, k-1

        while(right < len(sorted_nums)):
            minDif = min(minDif, sorted_nums[right] - sorted_nums[left])
            right+=1
            left+=1
        
        return minDif