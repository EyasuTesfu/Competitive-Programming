class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_edge(row, col):
            return (row == 0 or row == len(board)-1) or (col == 0 or col == len(board[0]) -1)
        vis = set()
        def is_valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row, col):
            vis.add((row, col))
            for r, c in directions:
                new_row = r + row
                new_col = c + col
                if is_valid(new_row, new_col):
                    if (new_row, new_col) not in vis:
                        if board[new_row][new_col] == "O":
                            board[new_row][new_col] = "NO"
                            dfs(new_row, new_col)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and is_edge(r, c) and (r, c) not in vis:
                    board[r][c] = "NO"
                    dfs(r, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "NO":
                    board[r][c] = "O"
        return board