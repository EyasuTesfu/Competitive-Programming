'''
Question link: https://leetcode.com/problems/minimum-size-subarray-sum/
Solution: using the variable size sliding window of pointers left and right'''
import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_arr = sys.maxsize
        _sum = 0
        while(right < len(nums)):
            _sum += nums[right]
            if _sum >= target:
                while(_sum >= target):
                    _sum -= nums[left]
                    left += 1
                min_arr = min(min_arr, (right-left) + 2)
            right += 1
        if min_arr > len(nums):
            return 0
        return min_arr
