class Solution:
    def largestNumber(self, nums: list[int]):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                str_holder1 = str(nums[i])+str(nums[j])
                str_holder2 = str(nums[j])+str(nums[i])
                if str_holder2 > str_holder1:
                    nums[i], nums[j] = nums[j], nums[i]
        nums = ''.join(map(str, nums))
        if nums[0] == '0':
            return '0'
        return nums
