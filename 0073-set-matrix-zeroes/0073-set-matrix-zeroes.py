class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                elif matrix[i][j] == 0:
                    k, l = i, j
                    while(k>=0):
                        matrix[k][j] = "0"
                        k -= 1
                    k = i
                    while(k<len(matrix)):
                        if matrix[k][j] == 0:
                            k += 1
                            continue
                        matrix[k][j] = "0"
                        k += 1
                    k = i
                    while(l >= 0):
                        matrix[i][l] = "0"
                        l -= 1
                    l = j
                    while(l < len(matrix[0])):
                        if matrix[i][l] == 0:
                            l += 1
                            continue
                        matrix[i][l] = "0"
                        l += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    
                    