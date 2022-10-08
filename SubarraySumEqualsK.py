class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        k_sub = _sum = 0
        prefix_sum = {0: 1}
        for i in nums:
            _sum += i
            if prefix_sum.get(_sum - k, 0) != 0:
                k_sub += prefix_sum[_sum-k]
            prefix_sum[_sum] = prefix_sum.get(_sum, 0) + 1
        return k_sub
