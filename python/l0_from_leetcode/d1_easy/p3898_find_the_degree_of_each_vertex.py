class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = []
        for vertex in matrix:
            result.append(sum(vertex))
        return result