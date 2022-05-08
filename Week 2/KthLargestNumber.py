class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(reverse=True, key=lambda x: int(x))
        return nums[k-1]
