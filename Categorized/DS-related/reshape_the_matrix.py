# problem link: https://leetcode.com/problems/reshape-the-matrix/description/
# time complexity: O(mn) or O(n^2)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # new_matrix = [[] for i in range(r)]
        # row, column = 0, 0
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if column == c:
        #             row += 1
        #             column = 0
        #         new_matrix[row].append(mat[i][j])
        #         column += 1
        # return new_matrix
        if len(mat) * len(mat[0]) != r*c:
            return mat  # this has to be on top for my code too...but the code below is better
        flat_array = []
        for i in mat:
            flat_array += i
        new_array = []
        for i in range(r):
            new_array.append(flat_array[c*i:c*(i+1)])
        return new_array
