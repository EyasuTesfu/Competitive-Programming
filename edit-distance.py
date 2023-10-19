class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0]+1
        for j in range(1, len(dp[0])):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete = dp[i][j-1] + 1
                    insert = dp[i-1][j] + 1
                    replace = dp[i-1][j-1] + 1
                    dp[i][j] = min(delete, insert, replace)
        return dp[-1][-1]