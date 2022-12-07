# problem link: https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan&id=data-structure-i
# time complexity: O(18)
# The code below is a nightmare, i was not focused when I wrote it and It pukes me to this day
# Never ever try to move a matrix across and from top to down at the same time(it's not worth it)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        thr_by_thr = {}
        i = j = r = c = 0
        while(i < 9 and j < 9):
            r = c = 0
            while(r < 9 and c < 9):
                if board[i][c].isdigit():
                    if i in row.keys():
                        if board[i][c] in row[i].keys():
                            return False
                        row[i][board[i][c]] = 1
                    else:
                        row[i] = {}
                        row[i][board[i][c]] = 1
                    if (i//3, c//3) not in thr_by_thr.keys():
                        thr_by_thr[(i//3, c//3)] = {}
                        thr_by_thr[(i//3, c//3)][board[i][c]] = (i, c)
                    else:
                        if board[i][c] in thr_by_thr[(i//3, c//3)].keys() and thr_by_thr[(i//3, c//3)][board[i][c]] != (i, c):
                            return False
                        thr_by_thr[(i//3, c//3)][board[i][c]] = (i, c)
                if board[r][j].isdigit():
                    if j in column.keys():
                        if board[r][j] in column[j].keys():
                            return False
                        column[j][board[r][j]] = 1
                    else:
                        column[j] = {}
                        column[j][board[r][j]] = 1
                    if (r//3, j//3) not in thr_by_thr.keys():
                        thr_by_thr[(r//3, j//3)] = {}
                        thr_by_thr[(r//3, j//3)][board[r][j]] = (r, j)
                    else:
                        if board[r][j] in thr_by_thr[(r//3, j//3)].keys() and thr_by_thr[(r//3, j//3)][board[r][j]] != (r, j):
                            return False
                        thr_by_thr[(r//3, j//3)][board[r][j]] = (r, j)
                r += 1
                c += 1
            i += 1
            j += 1
        return True
