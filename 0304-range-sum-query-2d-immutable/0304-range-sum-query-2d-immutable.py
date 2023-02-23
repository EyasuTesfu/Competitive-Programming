class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        inserted = [0] * len(matrix[0])
        matrix.insert(0, inserted)
        for i in range(len(matrix)):
            matrix[i].insert(0, 0)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2+1][col2+1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1] + self.matrix[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)