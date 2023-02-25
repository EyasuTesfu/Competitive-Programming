class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        max_subarray = float('-inf')
        _sum = 0
        while(right < len(nums)):
            _sum += nums[right]
            if right - left + 1 == k:
                max_subarray = max(max_subarray, _sum)
                _sum -= nums[left]
                left += 1
            right += 1
        return max_subarray/k