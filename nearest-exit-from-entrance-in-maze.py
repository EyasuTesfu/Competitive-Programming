class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] # right, down, up and left
        def is_valid(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == "."
        def is_edge(row, col):
            return row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) -1

        def bfs(_row, _col):
            vis = set()
            queue = deque()
            queue.append((_row, _col, 0))
            while queue:
                row, col, step = queue.popleft()
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if is_valid(new_row, new_col):
                        if [new_row, new_col] != entrance and is_edge(new_row, new_col):
                            return step + 1
                        if (new_row, new_col) not in vis:
                            queue.append((new_row, new_col, step + 1))
                            vis.add((new_row, new_col))
            return -1
        return bfs(entrance[0], entrance[1])