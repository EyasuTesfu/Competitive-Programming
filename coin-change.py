class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins, reverse = True)
        queue = deque()
        for coin in coins:
            if coin == amount:
                return 1
            if 0 < coin < amount:
                queue.append((coin, 1))
        vis = set()
        if len(queue) == 0:
            return -1
        while queue:
            pop_coin, length = queue.popleft()
            if pop_coin == amount:
                return length
            for coin in coins:
                new_val = coin + pop_coin
                if new_val == amount:
                    return length + 1
                if new_val < amount and new_val not in vis:
                    vis.add(new_val)
                    queue.append((new_val, length + 1))
        return -1