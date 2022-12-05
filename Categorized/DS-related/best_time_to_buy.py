# problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# time complexity: O(n)
# learnt how to make good use of conditionals
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in prices:
            if i <= min_price:
                min_price = i
            elif i - min_price > profit:
                profit = i - min_price
        return profit
