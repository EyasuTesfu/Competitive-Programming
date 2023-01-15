class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0
        for i in range(len(matrix)):
            if matrix[i][-1] == target:
                return True
            if matrix[i][-1] > target:
                target_row = i
                break
        for i in range(len(matrix[0])):
            if matrix[target_row][i] == target:
                return True
        return False