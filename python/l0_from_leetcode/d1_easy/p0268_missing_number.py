class Solution:
    # O(n) time and O(n) memory solution
    def missingNumber_baseApproach(self, nums: List[int]) -> int:
        numHash = set([i for i in range(0,len(nums)+1)])

        for i in nums:
            numHash.remove(i)

        return numHash.pop()
    
    def missingNumber_XOR_trick(self, nums: List[int]) -> int:
        # a ^ 0 = a; a ^ a = 0;
        xor = 0
        for ind,i in enumerate(nums):
            xor ^= ind ^ i
        xor ^= len(nums)

        return xor


