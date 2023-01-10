class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans