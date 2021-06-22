## 37. Sudoku Solver
## https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sudicti = {i:set(["1","2","3","4","5","6","7","8","9"]) for i in range(9)}
        sudictj = {j:set(["1","2","3","4","5","6","7","8","9"]) for j in range(9)}
        sudictk = {k:set(["1","2","3","4","5","6","7","8","9"]) for k in range(9)}
        options = {}
        # optioni = {}
        # optionj = {}
        # optionk = {}
        for i,row in enumerate(board):
            for j,row_col in enumerate(row):
                k = 3*(i//3)+(j//3)
                if row_col==".":
                    options.update({(i,j,k):set()})
                    # optioni[i] = {}
                    # optionj[j] = {}
                    # optionk[k] = {}
                else:
                    sudicti[i].discard(row_col)
                    sudictj[j].discard(row_col)
                    sudictk[k].discard(row_col)
        
        # dissolve = set()
        for i,j,k in options:
            options[(i,j,k)] = sudicti[i]&sudictj[j]&sudictk[k]
            # optioni[i].update({(j,k):1})
            # optionj[j].update({(i,k):1})
            # optionk[k].update({(i,j):1})
            # if len(options[(i,j,k)])==1:
            #     dissolve.add((i,j,k))
        
        # while dissolve:
        #     i,j,k = dissolve.pop()
        #     board[i][j] = options.pop((i,j,k)).pop()
        #     sudicti[i].discard(board[i][j])
        #     sudicti[j].discard(board[i][j])
        #     sudicti[k].discard(board[i][j])
        #     # options.pop((i,j,k))
        #     optioni[i].pop((j,k))
        #     optionj[j].pop((i,k))
        #     optionk[k].pop((i,j))
        #     if not(optioni[i]):
        #         optioni.pop(i)
        #     else:
        #         for nj,nk in optioni[i]:
        #             options[(i,nj,nk)].discard(board[i][j])
        #             if len(options[(i,nj,nk)])==1:
        #                 dissolve.add((i,nj,nk))
        #     if not(optionj[j]):
        #         optionj.pop(j)
        #     else:
        #         for ni,nk in optionj[j]:
        #             options[(ni,j,nk)].discard(board[i][j])
        #             if len(options[(ni,j,nk)])==1:
        #                 dissolve.add((ni,j,nk))
        #     if not(optionk[k]):
        #         optionk.pop(k)
        #     else:
        #         for ni,nj in optionk[k]:
        #             options[(ni,nj,k)].discard(board[i][j])
        #             if len(options[(ni,nj,k)])==1:
        #                 dissolve.add((ni,nj,k))
        
        # for i in range(9):
        #     eli = sudicti[i]
        #     if len(eli)==0:
        #         sudicti.pop(i)
        #     else:
        #         print(f"{len(eli)}:row={i}:{eli}")
        # for j in range(9):
        #     elj = sudictj[j]
        #     if len(elj)==0:
        #         sudictj.pop(j)
        #     else:
        #         print(f"{len(elj)}:col={j}:{elj}")
        # for k in range(9):
        #     elk = sudictk[k]
        #     if len(elk)==0:
        #         sudictk.pop(k)
        #     else:
        #         print(f"{len(elk)}:grd={k}:{elk}")
        
        # print(len(options))
        self.sudo_koo(board, options, sudicti, sudictj, sudictk)
        # print(len(options))
        
    def sudo_koo(self, board, options, sudicti, sudictj, sudictk):
        if len(options)==0:
            return True
        (i,j,k),ion = options.popitem()
        
        for elem in ion:
            if (elem in sudicti[i]&sudictj[j]&sudictk[k]):
                sudicti[i].remove(elem)
                sudictj[j].remove(elem)
                sudictk[k].remove(elem)
                if self.sudo_koo(board, options, sudicti, sudictj, sudictk):
                    board[i][j] = elem
                    return True
                else:
                    sudicti[i].add(elem)
                    sudictj[j].add(elem)
                    sudictk[k].add(elem)
            else:
                continue
        options[(i,j,k)] = ion
        return False
    