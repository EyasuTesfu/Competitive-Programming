class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        coins = 0
        piles.sort()
        for i in range(len(piles)-2, len(piles)//3 -1, -2):
                coins += piles[i]
        return coins