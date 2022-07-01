'''
Question link = https://leetcode.com/problems/next-greater-element-i/
Solution: ___EASY___'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        great_element = [-1] * len(nums1)
        for num in nums1:
            for _great in nums2[nums2.index(num):]:
                if _great > num:
                    great_element[nums1.index(num)] = _great
                    break
        return great_element
