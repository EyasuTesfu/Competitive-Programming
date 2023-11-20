class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = -1, -1
        right, bottom = len(matrix[0]), len(matrix)
        res = []
        while(len(res) < (len(matrix[0]) * len(matrix))):
            i = left + 1
            while(i < right):
                res.append(matrix[top+1][i])
                i += 1
            top += 1
            
            i = top + 1
            while(i < bottom):
                res.append(matrix[i][right-1])
                i += 1
            right -= 1
            if len(res) >= (len(matrix[0]) * len(matrix)):
                break
            i = right - 1
            while(i > left):
                res.append(matrix[bottom-1][i])
                i -= 1
            bottom -= 1
            print()

            i = bottom - 1
            while(i > top):
                res.append(matrix[i][left+1])
                i -= 1
            left += 1
        return res

