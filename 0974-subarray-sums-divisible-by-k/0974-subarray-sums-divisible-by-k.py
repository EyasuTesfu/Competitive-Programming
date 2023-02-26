class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_rem = {}
        res = 0
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum % k == 0:
                res += 1
            if _sum % k in prefix_rem:
                res += prefix_rem[_sum%k]
            prefix_rem[_sum%k] = prefix_rem.get(_sum%k, 0) + 1
        return res