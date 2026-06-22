class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowSet = set()
        left = 0
        for right in range(0, len(nums)):
            if ((right - left) > k):
                windowSet.remove(nums[left])
                left += 1
            if nums[right] in windowSet:
                return True
            else:
                windowSet.add(nums[right])
        return False
            
    def containsNearbyDuplicate_bruteForce_timesOut(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums) - 1):
            for j in range(i+1, min(len(nums), i+k+1)):
                if(nums[i] == nums[j]):
                    return True
        return False