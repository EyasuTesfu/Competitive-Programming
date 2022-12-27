# problem link: https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_p = m+n-1
        while(m > 0 and n > 0):
            if nums1[m-1] > nums2[n-1]:
                nums1[last_p] = nums1[m-1]
                m -= 1
            else:
                nums1[last_p] = nums2[n-1]
                n -= 1
            last_p -= 1
        # if there are leftovers
        while(n > 0):
            nums1[last_p] = nums2[n-1]
            n -= 1
            last_p -= 1
