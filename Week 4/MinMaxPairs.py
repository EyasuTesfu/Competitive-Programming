class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        min_pair = []
        n = len(nums)
        for i in range((n//2)):
            min_pair.append(nums[i]+nums[-1-i])
        return max(min_pair)


num1 = [3, 5, 2, 3]
print(Solution.minPairSum(Solution, nums=num1))
num1 = [3, 5, 4, 2, 4, 6]
print(Solution.minPairSum(Solution, nums=num1))
