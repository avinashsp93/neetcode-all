class NumMatrix:
    prefixMatrix = [[]]
    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (col + 1) for r in range(0, row+1)]
        for r in range(0,row):
            for c in range(0,col):
                self.prefixMatrix[r+1][c+1] = matrix[r][c] + self.prefixMatrix[r+1][c] + self.prefixMatrix[r][c+1] - self.prefixMatrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixMatrix[row2+1][col2+1] - (self.prefixMatrix[row1][col2+1] + self.prefixMatrix[row2+1][col1]) + self.prefixMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)