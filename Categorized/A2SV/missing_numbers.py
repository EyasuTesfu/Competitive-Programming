# problem link:https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_dict = {0: 0}
        n = len(nums)
        for i in range(1, n+1):
            sum_dict[i] = i + sum_dict[i-1]
        dif = sum_dict[n] - sum(nums)
        return dif
