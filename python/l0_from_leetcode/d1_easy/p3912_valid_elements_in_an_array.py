class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        leftGreatest,rightGreatest = [], []
        lg, rg = 0,0
        result = []

        for i in range(0,len(nums)):
            if(nums[i] > lg):
                lg = nums[i]
                leftGreatest.append(True)
            else:
                leftGreatest.append(False)
            
            j = len(nums) - i - 1
            if(nums[j] > rg):
                rg = nums[j]
                rightGreatest.append(True)
            else:
                rightGreatest.append(False)
            
            rightGreatest.reverse()


        for i in range(0,len(leftGreatest)):
            if(leftGreatest[i] or rightGreatest[i]):
                result.append(nums[i])
        
        return result