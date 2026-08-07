class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxCounter = 0
        for i in uniqueNums:
            if i-1 not in uniqueNums:
                counter = 1
                incrementer = i
                while(incrementer+1 in uniqueNums):
                    incrementer+=1
                    counter+=1
                maxCounter = max(maxCounter, counter)
        return maxCounter