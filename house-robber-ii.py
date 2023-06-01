class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        def dfs(curr_idx, nums1):
            if curr_idx == 0:
                return nums1[0]
            if curr_idx == 1:
                return max(nums1[0], nums1[1])
            if curr_idx not in self.memo:
                self.memo[curr_idx] = max(dfs(curr_idx-1, nums1), dfs(curr_idx-2, nums1)+nums1[curr_idx])
            return self.memo[curr_idx]
        n = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        val1 = dfs(n-1, nums[:-1])
        self.memo = {}
        val2 = dfs(n-1, nums[1:])
        return max(val1, val2)