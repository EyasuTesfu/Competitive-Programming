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
# ------------------Another approach---------------------


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_rows, ones_cols = [], []
        zeros_rows, zeros_cols = [], []
        for i in range(len(grid)):
            count = grid[i].count(1)
            ones_rows.append(count)
            zeros_rows.append(len(grid[0]) - count)
        for i in range(len(grid[0])):
            count = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    count += 1
            ones_cols.append(count)
            zeros_cols.append(len(grid) - count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = ones_rows[i] + ones_cols[j] - \
                    zeros_rows[i] - zeros_cols[j]
        return grid
