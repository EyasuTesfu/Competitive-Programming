# problem link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid_rows = {}
        grid_cols = {}
        output = [[] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i in grid_rows:
                        grid_rows[i] += 1
                    else:
                        grid_rows[i] = 1

                    if j in grid_cols:
                        grid_cols[j] += 1
                    else:
                        grid_cols[j] = 1
                else:
                    if i in grid_rows:
                        grid_rows[i] -= 1
                    else:
                        grid_rows[i] = -1

                    if j in grid_cols:
                        grid_cols[j] -= 1
                    else:
                        grid_cols[j] = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = grid_rows[i] + grid_cols[j]
                output[i].append(res)
        return output
