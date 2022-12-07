# problem link: https://leetcode.com/problems/pascals-triangle/description/
# time complexity: O(n*m)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_tri = [[1]]
        for i in range(1, numRows):
            pas_tri.append([1])
            for j in range(i-1):
                pas_tri[-1].append(pas_tri[-2][j] + pas_tri[-2][j+1])
            pas_tri[-1].append(1)
        return pas_tri
