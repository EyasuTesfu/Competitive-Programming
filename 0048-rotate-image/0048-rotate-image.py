class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0 , len(matrix)-1
        while(l < r):
            for i in range(r-l):
                holder = matrix[l+i][r]
                matrix[l+i][r] = matrix[l][l+i]
                holder2 = matrix[r][r-i]
                matrix[r][r-i] = holder
                holder = matrix[r-i][l]
                matrix[r-i][l] = holder2
                matrix[l][l+i] = holder
            l += 1
            r -= 1
        
                
        