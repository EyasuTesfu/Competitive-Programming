class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict()
        def dfs(idx, target):
            if idx >= len(nums) or target == 0:
                return target == 0
            val = (target, idx)
            if val not in memo:
                memo[val] = dfs(idx+1, target - nums[idx]) or dfs(idx+1, target)
            return memo[val]
        return sum(nums) % 2 == 0 and dfs(0, sum(nums) // 2)