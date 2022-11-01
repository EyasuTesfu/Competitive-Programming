class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])
        row = len(matrix)
        self.sum_val = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            prefix_sum = 0
            for j in range(col):
                prefix_sum += matrix[i][j]
                top_val = self.sum_val[i][j+1]
                self.sum_val[i+1][j+1] = prefix_sum + top_val
        # print(self.sum_val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        edge_val = self.sum_val[row2+1][col2+1]
        col_diduct = self.sum_val[row2+1][col1]
        row_diduct = self.sum_val[row1][col2+1]
        result = edge_val - (col_diduct+row_diduct) + self.sum_val[row1][col1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
