class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target in nums:
                return 0
            return -1
        right_half = []
        left_half = []
        i = 1
        while i < len(nums):
            if nums[i] - nums[i-1] < 0:
                right_half = nums[:i]
                left_half = nums[i:]
                break
            i += 1
        if i == len(nums):
            sorted_array = nums
        else:
            sorted_array = left_half + right_half
        l = 0
        r = len(sorted_array) - 1
        while l <= r:
            mid = l + (r-l)//2
            if sorted_array[mid] == target:
                return nums.index(target)
            elif sorted_array[mid] > target:
                r = mid-1
            else:
                l = mid + 1
        
        return -1
            