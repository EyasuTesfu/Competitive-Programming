class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        _sum = 0
        left = 0
        for i in range(len(nums)):
            _sum += nums[i]
            while _sum >= target:
                res = min(res, i - left+1)
                _sum -= nums[left]
                left += 1
        if res > len(nums):
            return 0
        return res