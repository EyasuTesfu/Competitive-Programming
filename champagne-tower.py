class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pour_pyramid = [[0] * k for k in range(1, 102)]
        pour_pyramid[0][0] = poured

        for i in range(query_row+1):
            for j in range(i+1):
                pour_value = (pour_pyramid[i][j] - 1.0) / 2.0
                if pour_value > 0:
                    pour_pyramid[i+1][j] += pour_value
                    pour_pyramid[i+1][j+1] += pour_value
        return min(1, pour_pyramid[query_row][query_glass])