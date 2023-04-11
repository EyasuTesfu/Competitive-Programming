class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        size = 0
        # find the size
        for edge in edges:
            size = max(edge[0], edge[1], size)

        # instantiante your grid
        grid = [[0 for _ in range(size)] for _ in range(size)]
        for edge in edges:
            grid[edge[0]-1][edge[1]-1] = 1
            grid[edge[1]-1][edge[0]-1] = 1

        for row in range(size):
            star = True
            for col in range(size):
                if col == row: continue
                if grid[row][col] == 0:
                    star = False
            if star == True:
                return row+1
        return 0