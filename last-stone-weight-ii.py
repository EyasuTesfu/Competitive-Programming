class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        def dp(i, s):
            if (i, s) in memo:
                return memo[(i, s)]
            if i == len(stones):
                memo[(i, s)] = s
                return s
            ans1 = dp(i+1, s+ stones[i])
            ans2 = dp(i+1, s-stones[i])
            if ans1 < 0:
                ans1 = float('inf')
            if ans2 < 0:
                ans2 = float('inf')
            res = min(ans1, ans2)
            memo[(i, s)] = res
            return res
        return dp(0, 0)