# problem link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=study-plan&id=data-structure-i
# time complexity: O(n) 97% faster when turning line no.8 from:
# nums1_dict.get(i, "x") != x to i in nums1_dict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = Counter(nums1)
        result = []
        for i in nums2:
            if i in nums1_dict and nums1_dict[i] > 0:
                result.append(i)
                nums1_dict[i] -= 1
        return result
