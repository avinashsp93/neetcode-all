class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_tri = [[1]]
        for i in range(1, numRows):
            tempArray = [0, *pas_tri[i-1], 0]
            result = []
            for j in range(0, len(tempArray) - 1):
                result.append(tempArray[j] + tempArray[j+1])
            pas_tri.append(result)
        return pas_tri