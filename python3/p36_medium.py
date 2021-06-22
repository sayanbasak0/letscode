## 36. Valid Sudoku
## https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudictrow = [set() for i in range(9)]
        sudictcol = [set() for i in range(9)]
        sudictgrd = [set() for i in range(9)]
        for i,row in enumerate(board):
            for j,row_col in enumerate(row):
                if row_col==".":
                    continue
                if row_col in sudictrow[i]:
                    return False
                else:
                    sudictrow[i].add(row_col)
                if row_col in sudictcol[j]:
                    return False
                else:
                    sudictcol[j].add(row_col)
                k = 3*(i//3)+(j//3)
                if row_col in sudictgrd[k]:
                    return False
                else:
                    sudictgrd[k].add(row_col)
        return True