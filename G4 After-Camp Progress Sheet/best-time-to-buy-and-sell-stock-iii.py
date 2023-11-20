class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, bought, count):
            if idx == len(prices):
                return 0
            if count == 2:
                return 0

            passed = dfs(idx+1, bought, count)

            if bought:
                return max(passed, dfs(idx+1, not bought, count+1) + prices[idx])
            else:
                return max(passed, dfs(idx+1, not bought, count) - prices[idx])
        
        return dfs(0, False, 0)