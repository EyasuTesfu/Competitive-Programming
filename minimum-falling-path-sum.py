class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        sum_matrix = [[float('inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        sum_matrix[0] = matrix[0]
        def valid(row, col):
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                return True
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if valid(i+1, j-1):
                    val = sum_matrix[i][j] + matrix[i+1][j-1]
                    if sum_matrix[i+1][j-1] == float('inf') or val < sum_matrix[i+1][j-1]:
                        sum_matrix[i+1][j-1] = val
                if valid(i+1, j):
                    val = sum_matrix[i][j] + matrix[i+1][j]
                    if sum_matrix[i+1][j] == float('inf') or val < sum_matrix[i+1][j]:
                        sum_matrix[i+1][j] = val

                if valid(i+1, j+1):
                    val = sum_matrix[i][j] + matrix[i+1][j+1]
                    if sum_matrix[i+1][j+1] == float('inf') or val < sum_matrix[i+1][j+1]:
                        sum_matrix[i+1][j+1] = val
        return min(sum_matrix[-1])