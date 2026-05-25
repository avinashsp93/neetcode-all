from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0, 9):
            rowWiseSet = set()
            columnWiseSet = set()
            for j in range(0, 9):
                if board[i][j] not in rowWiseSet:
                    if not board[i][j] == ".":
                        rowWiseSet.add(board[i][j])
                else:
                    return False
                
                if board[j][i] not in columnWiseSet:
                    if not board[j][i] == ".":
                        columnWiseSet.add(board[j][i])
                else:
                    return False
                
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxWiseSet = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] not in boxWiseSet:
                            if not board[k][l] == ".":
                                boxWiseSet.add(board[k][l])
                        else:
                            return False
        
        return True

                