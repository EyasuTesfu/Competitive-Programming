class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = sum(nums[:k])
        i, j = 0, k
        max_sum = _sum
        while j < len(nums):
            _sum = _sum - nums[i] + nums[j]
            max_sum = max(max_sum , _sum)
            i += 1
            j += 1
        return max_sum/k