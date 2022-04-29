class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for _num in nums:
            count = 0
            for i in range(len(nums)):
                if _num > nums[i]:
                    count += 1
            lst.append(count)
        return lst
