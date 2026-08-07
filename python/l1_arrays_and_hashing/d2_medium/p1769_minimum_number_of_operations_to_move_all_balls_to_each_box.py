class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        for index, i in enumerate(list(boxes)):
            if int(i) == 1:
                boxLocations.append(index)

        result = []
        for j in range(0, len(boxes)):
            agg = 0
            for k in boxLocations:
                agg += abs(j-k)
            result.append(agg)
        return result