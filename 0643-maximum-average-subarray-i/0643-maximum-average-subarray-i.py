class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        i, j = 0, k
        m = s
        while j < len(nums):
            s = s - nums[i] + nums[j]
            m = max(m , s)
            i += 1
            j += 1
        return m/k