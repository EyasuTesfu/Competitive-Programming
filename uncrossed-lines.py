class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == len(nums1):
                return 0
            if j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
               memo[(i, j)] = 1 + dp(i+1, j+1)
            else:
                memo[(i,j)] = max(dp(i+1, j), dp(i, j+1))
            return memo[(i,j)]
        return dp(0, 0)