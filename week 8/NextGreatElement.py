'''
Question link = https://leetcode.com/problems/next-greater-element-i/
Solution1: ___EASY___BruteForce Solution
Solution2: ___Medium__Stack Solution'''
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

# Below is a faster solution O(n + m) time complexity and a O(m) space complexity using stack


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_index = {num: i for i, num in enumerate(nums1)}
        stack = []
        great_element = [-1] * len(nums1)
        for num in nums2:
            if stack and num > stack[-1]:
                while(stack and num > stack[-1]):
                    great_element[num_index[stack[-1]]] = num
                    stack.pop()
            if num in nums1:
                stack.append(num)
        return great_element
