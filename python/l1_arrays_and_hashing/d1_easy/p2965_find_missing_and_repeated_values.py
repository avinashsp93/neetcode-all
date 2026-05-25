class Solution:
    def findMissingAndRepeatedValues_hashSet(self, grid: List[List[int]]) -> List[int]:
        allElementsHash = set(range(1, (len(grid)*len(grid)) + 1))
        repeatAndMissed = [0,0]
        for element in grid:
            for j in element:
                if j in allElementsHash:
                    allElementsHash.remove(j)
                else:
                    repeatAndMissed[0] = j
        repeatAndMissed[1] = allElementsHash.pop()
        return repeatAndMissed
