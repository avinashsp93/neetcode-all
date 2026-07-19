class Solution:
    # O(nlog(n)) : Using built-in sort
    def heightChecker(self, heights: List[int]) -> int:
        mismatchCount = 0
        sortedHeights = sorted(heights)

        for i in range(0, len(sortedHeights)):
            if(sortedHeights[i] != heights[i]):
                mismatchCount +=1
        return mismatchCount
                
    # O(n) : Using bucket sort
    def heightChecker_bucketSort(self, heights: List[int]) -> int:
        mismatchCount = 0
        bucket = [0] * 101
        sortedHeights = []

        for h in heights:
            bucket[h] += 1
        
        for b in range(1, 101):
            c = bucket[b]
            while(c):
                sortedHeights.append(b)
                c-=1
        
        for i in range(0, len(sortedHeights)):
            if(sortedHeights[i] != heights[i]):
                mismatchCount +=1
        return mismatchCount
