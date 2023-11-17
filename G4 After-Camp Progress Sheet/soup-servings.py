class Solution:
    def soupServings(self, n: int) -> float:
        memo = {}
        m = math.ceil(n/25)
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if b <= 0:
                return 0
            if a <= 0:
                return 1
            curr = 0
            memo[(a,b)] = (dp(a - 4, b) + dp(a- 3, b-1) + dp(a-2, b-2) + dp(a-1, b-3))/4
            return memo[(a, b)]
        for k in range(1, m+1):
            if dp(k, k) > 1 - 1e-5:
                return 1.0
        return dp(m, m)
            
