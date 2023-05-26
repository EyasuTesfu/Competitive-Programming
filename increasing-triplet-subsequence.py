class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        _min = nums[0]
        double = None
        for i in range(1, len(nums)):
            if nums[i] <= _min:
                _min = nums[i]
            else:
                if double:
                    if double[1] < nums[i]:
                        return True
                double = (_min, nums[i])
        return False