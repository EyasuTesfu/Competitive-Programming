class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def dp(k, r, c):
            if r >= n or c >= n or r < 0 or c < 0:
                return 0
            if k == 0:
                return 1
            directions = [(-1,-2), (-2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1)]
            pr = 0
            for row, col in directions:
                new_row = row + r
                new_col = col + c
                pr += dp(k-1, new_row, new_col)/8.0
            return pr
        return dp(k, row, column)