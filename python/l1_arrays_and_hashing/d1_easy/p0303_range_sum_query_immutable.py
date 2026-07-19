class NumArray:
    prefixSumArray = []
    def __init__(self, nums: List[int]):
        prefixSum = 0
        for i in nums:
            prefixSum += i
            self.prefixSumArray.append(prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSumArray[right]
        return self.prefixSumArray[right] - self.prefixSumArray[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)