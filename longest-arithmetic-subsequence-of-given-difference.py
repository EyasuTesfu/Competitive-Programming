class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            diff = num - difference
            dp[num] = dp[diff] + 1
        return max(dp.values())