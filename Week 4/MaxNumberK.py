from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        amount = Counter(nums)
        x = count = 0
        for i in range(len(nums)):
            x = k-nums[i]
            amount[nums[i]] -= 1
            if amount[x] > 0 and amount[nums[i]] >= 0:
                amount[x] -= 1
                count += 1
        return count
