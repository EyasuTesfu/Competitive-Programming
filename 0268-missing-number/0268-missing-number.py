class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0, n]
        nums.append(-1)
        i = 0
        while i < len(nums):
            pos = nums[i]
            if nums[i] != -1 and nums[i] != i:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        return nums.index(-1)