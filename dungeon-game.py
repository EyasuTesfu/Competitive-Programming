class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float('inf')]*len(dungeon[0]) for _ in range(len(dungeon))]
        
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if i == len(dungeon)- 1 and j == len(dungeon[0])-1:
                    dp[i][j] = min(0, dungeon[i][j])
                elif i == len(dungeon) - 1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j+1])
                elif j == len(dungeon[0]) - 1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i+1][j])
                else:
                    dp[i][j] = min(0, max(dp[i+1][j], dp[i][j+1])+dungeon[i][j])
        
        return abs(dp[0][0]) + 1