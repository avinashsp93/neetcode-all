class Solution:
    def singleNonDuplicate_BigO_N(self, nums: List[int]) -> int:
        my_set = set()
        for i in nums:
            if i in my_set:
                my_set.remove(i)
            else:
                my_set.add(i)
        return my_set.pop()

    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        if len(nums) == 1:
            return nums[0]
        
        while(low <= high):
            mid = (low + high)//2
            leftMid = mid - 1
            rightMid = mid + 1
            
            # corner case
            if((leftMid < 0 and nums[mid] != nums[rightMid]) or (rightMid > len(nums)-1 and nums[mid] != nums[leftMid])):
                return nums[mid]

            if(nums[leftMid] != nums[mid] and nums[rightMid] != nums[mid]):
                return nums[mid]
            elif(nums[mid-1] == nums[mid]):
                secondMidIndex = mid - 1  
            else:
                secondMidIndex = mid + 1
            
            if(min(mid, secondMidIndex) - low) % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0