class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        evenC, oddC = 0, 0
        par = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] % 2 == 0:
                par.append(oddC)
                evenC += 1
            else:
                par.append(evenC)
                oddC += 1
        par.reverse()
        return par