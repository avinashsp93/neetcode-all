class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        (candidate, count) = self.majorityElement(nums)
        leftMajor, rightMajor = 0, count
        numsLength = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == candidate:
                leftMajor += 1
                rightMajor -= 1
            print(leftMajor, (i+1), rightMajor, (numsLength-i-1))
            if(leftMajor/(i+1) > 0.5 and rightMajor/(numsLength-i-1) > 0.5):
                return i                     
        return -1

    def majorityElement(self, nums) -> (int,int):
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        count = nums.count(candidate)
        return (candidate, count)