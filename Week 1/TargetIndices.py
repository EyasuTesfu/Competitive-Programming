class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        lst = []
        start_at = 0
        for num in nums:
            if num == target:
                lst.append(nums.index(num, start_at))
            start_at += 1
        lst = sorted(lst)
        return lst
