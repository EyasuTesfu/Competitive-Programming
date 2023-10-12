class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        res = acc = 0
        for x in nums:
            if acc: acc &= x
            else: acc, res = x, res + 1
        return max(1, res - bool(acc))