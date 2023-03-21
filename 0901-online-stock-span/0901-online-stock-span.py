class StockSpanner:

    def __init__(self):
        self.stack = [] # monotonically decreasing stack, holding how many smaller where just before this one

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append([price, count])
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)