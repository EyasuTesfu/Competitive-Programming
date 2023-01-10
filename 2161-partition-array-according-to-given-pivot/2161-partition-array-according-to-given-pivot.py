class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        medium = []
        large = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                small.append(nums[i])
            elif nums[i] == pivot:
                medium.append(nums[i])
            else:
                large.append(nums[i])
        return small + medium + large
            