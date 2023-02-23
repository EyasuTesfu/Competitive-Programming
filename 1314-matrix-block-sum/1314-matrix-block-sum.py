class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        mat.append([0]*cols)
        for row in mat:
            row.append(0)
        for i in range(rows):
            for j in range(cols):
                mat[i][j] += mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]
        ans = [[0]* cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # r, l, u, d
                r = min(j+k, cols-1)
                l = max(j-k, 0)
                u = max(i-k, 0)
                d = min(i+k, rows-1)
                res = mat[d][r] - mat[d][l-1] - mat[u-1][r] + mat[u-1][l-1]
                ans[i][j] = res
        return ans