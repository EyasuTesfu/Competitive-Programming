class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        for val in range(1, target+1):
            for num in nums:
                memo[val] += memo[val-num]
        return memo[target]