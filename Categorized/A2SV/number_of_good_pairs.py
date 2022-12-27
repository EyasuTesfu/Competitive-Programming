# problem link: https://leetcode.com/problems/number-of-good-pairs/description/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        pairs = {}
        for i in range(len(nums)):
            if pairs.get(nums[i], None) == None:
                pairs[nums[i]] = 1
            else:
                good_pairs += pairs[nums[i]]
                pairs[nums[i]] += 1
        return good_pairs
