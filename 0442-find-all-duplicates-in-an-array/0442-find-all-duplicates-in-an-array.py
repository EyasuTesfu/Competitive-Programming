class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            pos = nums[i]-1
            if nums[i] - 1 != i and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
                
        res = []
        for i in range(len(nums)):
            if nums[i]-1 != i:
                res.append(nums[i])
        return res