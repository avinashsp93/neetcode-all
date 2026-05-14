class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterMap = dict()
        for i in range(0,len(nums2)-1):
            nextGreaterFound = False
            for j in range(i+1, len(nums2)):
                if(nums2[i] < nums2[j]):
                    nextGreaterFound = True
                    nextGreaterMap[nums2[i]] = nums2[j]
                    break
            if nextGreaterFound == False:
                nextGreaterMap[nums2[i]] = -1
        result = []
        for k in nums1:
            result.append(nextGreaterMap.get(k, -1))
        return result