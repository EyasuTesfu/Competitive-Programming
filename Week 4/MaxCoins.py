# [9,8,7,6,5,4,3,2,1]
# (9,8,7) = 8
# (6,5,4) = 5 = 13
# (3,2,1) = 2 = 15
# (9,8,1) = 8
# (7,6,2) = 6 = 14
# (5,4,3) = 4 = 18
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        coins = 0
        piles.sort()
        for i in range(len(piles)-2, len(piles)//3 - 1, -2):
            coins += piles[i]
        return coins


# pile1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# print(Solution.maxCoins(Solution, piles=pile1))
# pile1 = [2, 4, 5]

# print(Solution.maxCoins(Solution, piles=pile1))
# pile1 = [4, 4, 17, 7, 16, 16, 16, 15, 2, 3, 1, 17, 6, 12, 9]

# print(Solution.maxCoins(Solution, piles=pile1))
