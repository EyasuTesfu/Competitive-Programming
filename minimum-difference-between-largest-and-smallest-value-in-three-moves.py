class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        else:
            nums = sorted(nums)
            _min = sys.maxsize
            _min = min(_min, nums[-1]-nums[3])
            _min = min(_min, nums[-2]-nums[2])
            _min = min(_min, nums[-3]-nums[1])
            _min = min(_min, nums[-4]-nums[0])
            return _min