class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cool_down = -float('inf'), 0, 0
        for price in prices:
            prev_buy, prev_sell, prev_cool_down = buy, sell, cool_down
            buy = max(prev_cool_down - price, prev_buy)
            sell = prev_buy + price
            cool_down = max(prev_sell, prev_cool_down)
        return max(sell, cool_down)