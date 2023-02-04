class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def thr_by_thr(a,b,c,
                      d,e,f,
                      g,h,i):
            return (reduce(lambda a, b: a + 1 if -1< b < 10 else 0, set([a,b,c,d,e,f,g,h,i]), 0) == 9 and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))
        count = 0
        for i in range(m-2):
            for j in range(n-2):
                if thr_by_thr(grid[i][j], grid[i][j+1], grid[i][j+2],
                          grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                          grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]): count += 1
        return count