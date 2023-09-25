class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 1 - 6 up
        # 1, 2, 3, 4, 5, 6 all these options in the queue and then count the steps
        n = len(board)
        vis = set()
        def row_col(position):
            row = (n - 1) - (position-1) // n
            col = (position - 1) % n
            if row % 2 == (n-1) % 2:
                return (row, col)
            else:
                return (row, n-1-col)
        
        queue = deque()
        queue.append((1, 0)) # position, step
        vis.add(1)
        while queue:
            pos, step = queue.popleft()
            if pos == n**2:
                return step
            
            for i in range(1, 7):
                new_pos = pos + i
                if new_pos > n**2:
                    break
                new_row, new_col = row_col(new_pos)
                if (new_row, new_col) not in vis:
                    vis.add((new_row, new_col))
                    if board[new_row][new_col] == -1:
                        queue.append((new_pos, step + 1))
                    else:
                        queue.append((board[new_row][new_col], step + 1))
        return -1