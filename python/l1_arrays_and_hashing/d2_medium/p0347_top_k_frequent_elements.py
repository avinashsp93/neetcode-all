from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOccurrences = Counter(nums)
        result = []
        bucket = [[] for i in range(0, len(nums)+1)]

        for key,val in numOccurrences.items():
            bucket[val].append(key)

        for b in range(len(bucket)-1, -1, -1):
            if len(bucket[b]) != 0:
                for ele in bucket[b]:
                    result.append(ele)
            k-=len(bucket[b])
            if k <= 0:
                return result
        return result