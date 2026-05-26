class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ 0 = a; a ^ a = 0;
        xor = 0
        for i in nums:
            xor ^= i
        return xor