class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum = 0
        _max = float('-inf')
        for i in range(len(nums)):
            _max = max(pref_sum + nums[i],_max)
            pref_sum = max(pref_sum + nums[i], 0)
        return _max