class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        
        max_area = 0
        vis = set()
        def dfs(row, col):
            vis.add((row, col))
            area = 0
            for r, c in directions:
                new_row = r + row
                new_col = c + col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in vis:
                    if grid[new_row][new_col] == 1:
                        area += dfs(new_row, new_col) + 1
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in vis:
                    if grid[i][j] == 1:
                        max_area = max(max_area, 1 + dfs(i, j))
        return max_area