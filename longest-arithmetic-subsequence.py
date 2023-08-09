class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        left = right = 0
        dp = defaultdict(tuple)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
        return max(dp.values())