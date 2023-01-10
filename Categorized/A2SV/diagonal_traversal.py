# problem link: https://leetcode.com/problems/diagonal-traverse/description/
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = []
        cur_row, cur_col = 0, 0
        going_up = True
        going_down = False
        while len(diagonal) != len(mat) * len(mat[0]):
            if going_up:
                while(cur_row >= 0 and cur_col < len(mat[0])):
                    diagonal.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == len(mat[0]):
                    cur_row += 2
                    cur_col -= 1
                elif cur_row < 0:
                    cur_row += 1
                going_up = False
                going_down = True

            elif going_down:
                while(cur_col >= 0 and cur_row < len(mat)):
                    diagonal.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                if cur_row == len(mat):
                    cur_col += 2
                    cur_row -= 1
                elif cur_col < 0:
                    cur_col += 1
                going_up = True
                going_down = False

        return diagonal
