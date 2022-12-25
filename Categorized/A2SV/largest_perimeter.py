# problem link: https://leetcode.com/problems/largest-perimeter-triangle/description/?
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        max_per = 0
        while(i < len(nums)-2):
            _sum = sum(nums[i:i+2])
            if _sum > nums[i+2]:
                max_per = max(max_per, _sum + nums[i+2])
            i += 1
        return max_per
