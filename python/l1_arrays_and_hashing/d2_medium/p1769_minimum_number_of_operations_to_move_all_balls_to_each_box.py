class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(box) for box in boxes.split('')]
        boxLocations = []
        for index, i in enumerate(boxes):
            if i == 1:
                boxLocations.append(index)

        result = []
        for j in range(0, len(boxes)):
            agg = 0
            for k in boxLocations:
                agg += abs(j-k)
            result.append(agg)
        return result