class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set(nums)
        for i in nums:
            distinct.add(int(str(i)[::-1]))
        return len(distinct)