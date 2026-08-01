from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOccurrences = Counter(nums)
        bucket = [[] for i in range(0, len(nums)+1)]

        