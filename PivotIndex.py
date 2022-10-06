class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        _sum = sum(nums)
        for i in range(len(nums)):
            if left == _sum - nums[i]:
                return i
            _sum -= nums[i]
            left += nums[i]
        return -1
