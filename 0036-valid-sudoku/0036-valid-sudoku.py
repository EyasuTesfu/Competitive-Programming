class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return True
        mat = [[[] for _ in range(3)] for _ in range(3)]

        # row
        for i in range(9):
            vis = set()
            for j in range(9):
                if board[i][j] in vis:
                    return False
                if board[i][j] != ".":
                    vis.add(board[i][j])
        
        # col
        for i in range(9):
            vis = set()
            for j in range(9):
                if board[j][i] in vis:
                    return False
                if board[j][i] != ".":
                    vis.add(board[j][i])
        
        # 3 x 3
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    mat[i//3][j//3].append(board[i][j])
        
        for i in range(3):
            for j in range(3):
                if len(set(mat[i][j])) != len(mat[i][j]):
                    return False
        return True