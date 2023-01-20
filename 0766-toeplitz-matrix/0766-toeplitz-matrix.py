class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            k = i
            j = 0
            num = matrix[k][j]
            while(k < len(matrix) and j < len(matrix[0])):
                if matrix[k][j] != num:
                    return False
                k += 1
                j += 1
        for j in range(1,len(matrix[0])):
            k = j
            i = 0
            num = matrix[i][k]
            while(k < len(matrix[0]) and i < len(matrix)):
                if matrix[i][k] != num:
                    return False
                k += 1
                i += 1
        return True