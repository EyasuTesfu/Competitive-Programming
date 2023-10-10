class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        movements = [(1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
        memo = {}
        exception = (3, 1)
        def dp(r, c, count):
            if (r, c, count) in memo:
                return memo[(r,c, count)]
            if count == n:
                return 1
            cur = 0
            for row, col in movements:
                new_row = r + row
                new_col = c + col
                if (0 <= new_row < 3 and 0 <= new_col < 3) or (new_row, new_col) == exception:
                    cur += dp(new_row, new_col, count + 1)
            memo[(r, c, count)] = cur % (10**9 + 7)
            return cur
        _sum = 0
        for i in range(3):
            for j in range(3):
                _sum += dp(i, j, 1)
        _sum += dp(3, 1, 1)
        
        return _sum % (10**9 + 7)