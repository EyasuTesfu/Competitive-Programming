class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        j = k
        m = s
        while j < len(nums):
            s = s - nums[j-k] + nums[j]
            m = max(m , s)
            j += 1
        return m/k