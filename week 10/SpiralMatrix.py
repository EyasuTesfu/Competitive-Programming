
'''
Question link: https://leetcode.com/problems/spiral-matrix/
Solution: simulate the spiral matrix one time and try to imagine doing it for the 
rest of the rectangles formed inside the spiral matrix'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_array = []
        top = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        while(top < bottom and left < right):
            for i in range(left, right):
                spiral_array.append(matrix[top][i])
            top += 1
            for j in range(top, bottom):
                spiral_array.append(matrix[j][right-1])
            right -= 1
            if not (top < bottom and left < right):
                break
            for i in reversed(range(left, right)):
                spiral_array.append(matrix[bottom-1][i])
            bottom -= 1
            for j in reversed(range(top, bottom)):
                spiral_array.append(matrix[j][left])
            left += 1
        return spiral_array  # t 2 m 2 i 1, l 1 n 2 j 1,
