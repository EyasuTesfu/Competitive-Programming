class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = left
        k = 1
        if len(nums) ==  1:
            return 1
        for left in range(1,len(nums)):
            if right >= len(nums):
                return k
            if nums[right] > nums[left]:
                nums[left] = nums[right]
            if nums[left] == nums[left-1]:
                if nums[right] == nums[left]:
                    while(right < len(nums) and nums[right] == nums[left]):
                        right += 1
                    if right == len(nums):
                        return k
                    nums[left] = nums[right]
            right += 1
            k += 1