# problem link: https://leetcode.com/problems/contains-duplicate/description/
# --------------------------------Sorting------------------------------------
# time complexity = O(n) space complexity = O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1:
            return False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
# --------------------------------HashMap-------------------------------------
# time complexity = O(n) space complexity = O(1)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        my_dict = {}
        for i in nums:
            if my_dict.get(i, "x") == "x":
                my_dict[i] = 1
            else:
                return True
        return False
# --------------------------------Set------------------------------------------
# time complexity = O(n) space complexity = O(1)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            my_set.add(i)
        return False
# --------------------------------Checked Length Set----------------------------
# time complexity = O(n) space complexity = O(1)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
