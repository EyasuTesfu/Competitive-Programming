class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1 if i == 0 or j == 0 else 0 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[-1][-1]