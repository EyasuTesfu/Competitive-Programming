class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        vis = set()
        def dfs(r, c):
            vis.add((r,c))
            if board[r][c] == "M":
                board[r][c] = "X"
                return
            count = 0
            for row, col in directions:
                new_row = row + r
                new_col = col + c
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if (new_row, new_col) not in vis:
                        if board[new_row][new_col] == "M":
                            count += 1
            if count:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"

            if board[r][c] == "B":
                for row, col in directions:
                    new_row = row + r
                    new_col = col + c
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                        if (new_row, new_col) not in vis:
                            if board[new_row][new_col] != "M":
                                dfs(new_row, new_col)
        dfs(click[0], click[1])
        return board