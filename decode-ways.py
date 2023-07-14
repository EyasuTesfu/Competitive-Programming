class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(s):
            if not s:
                return 1
            first, second = 0, 0
            if 1 <= int(s[:1]) <= 9:
                first = dp(s[1:])
            if 10 <= int(s[:2]) <= 26:
                second = dp(s[2:])
            return first + second
        return dp(s)