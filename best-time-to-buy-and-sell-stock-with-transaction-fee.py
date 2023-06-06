class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        def dfs(idx, bought):
            if idx == len(prices):
                return 0
            
            passed = dfs(idx+1, bought)
            if bought:
                return max(passed, dfs(idx+1, not bought) + (prices[idx] - fee))
            else:
                return max(passed, dfs(idx+1, not bought) - prices[idx])
            
        return dfs(0, False)