def sortColors(nums) -> None:
    for i in range(len(nums)-1):
        for k in range(i, len(nums)):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
