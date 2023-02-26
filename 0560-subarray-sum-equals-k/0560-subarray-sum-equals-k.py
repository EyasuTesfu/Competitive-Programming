class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        _sum = 0
        prefix_sum = {}
        ans = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum == k:
                ans += 1
            if _sum-k in prefix_sum:
                ans += prefix_sum[_sum-k]
            prefix_sum[_sum] = prefix_sum.get(_sum, 0) + 1
        return ans