# problem link: https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_m = left_n = 0
        right_m = len(matrix)-1
        right_n = len(matrix[0])-1
        while(left_m <= right_m):
            mid = (left_m + right_m)//2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right_m = mid-1
            else:
                left_m = mid + 1
        while(left_n <= right_n):
            mid = (left_n + right_n)//2
            if matrix[right_m][mid] == target:
                return True
            if matrix[right_m][mid] > target:
                right_n = mid-1
            else:
                left_n = mid + 1
        return False
