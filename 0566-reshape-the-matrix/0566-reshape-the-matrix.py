class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r*c:
            return mat
        flat_array = []
        for i in mat:
            flat_array += i
        new_array = []
        for i in range(r):
            new_array.append(flat_array[c*i:c*(i+1)])
        return new_array