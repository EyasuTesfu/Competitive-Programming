class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 2]
        for i in range(3 ,n+1):
            curr = 0
            for j in range(1,i+1):
                right = i-j
                left = i-right-1
                if left == 0:
                    curr += dp[right-1]
                elif right == 0:
                    curr += dp[left-1]
                else:
                    curr += dp[right-1]*dp[left-1]
            dp.append(curr)
        return dp[n-1]