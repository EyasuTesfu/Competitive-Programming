class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        vis = set()
        directions = [(0,1),(0,-1), (1, 0), (-1,0)]
        def dfs(r, c, temp_bool):
            if grid1[r][c] != 1:
                temp_bool = False
            vis.add((r, c))
            for row, col in directions:
                new_row = row + r
                new_col = col + c
                if 0 <= new_row < len(grid2) and 0 <= new_col < len(grid2[0]) and grid2[new_row][new_col] == 1:
                    if (new_row, new_col) not in vis:
                        temp_bool &= dfs(new_row, new_col, temp_bool)
            return temp_bool
        res = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1 and (r,c) not in vis:
                    if dfs(r, c, True):
                        res += 1
        return res