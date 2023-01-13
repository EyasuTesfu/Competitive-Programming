class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        i = 0
        max_sum = 0
        while(i + 2 < len(grid)):
            j = 0
            while(j+2 < len(grid[0])):
                _sum = grid[i][j+1] + grid[i+2][j+1] + grid[i][j] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+2][j]
                max_sum = max(max_sum, _sum)
                j += 1
            i += 1
        return max_sum