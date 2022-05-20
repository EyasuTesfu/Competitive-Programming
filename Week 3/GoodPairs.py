class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

#
#
# Best approach would be using a dictionary which would be O(n)


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs = 0
        pairs = {}
        for i in range(len(nums)):
            if pairs.get(nums[i], None) == None:
                pairs[nums[i]] = 1
            else:
                good_pairs += pairs[nums[i]]
                pairs[nums[i]] += 1
        return good_pairs
