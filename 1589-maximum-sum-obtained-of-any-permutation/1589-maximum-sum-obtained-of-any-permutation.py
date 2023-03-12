class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # [1, 2, 1, 1, 0] => [1, 2, 3, 4, 5]
        # [2, 5, 4, 3, 1]
        # [5, 4, 3, 2, 1]
        # [2, 1, 1, 1, 0]
        prefix_req = [0]*(len(nums)+1)
        for i in range(len(requests)):
            prefix_req[requests[i][0]] += 1
            prefix_req[requests[i][1]+1] -= 1
            
        # sum the prefix values
        for i in range(1,len(nums)+1):
            prefix_req[i] += prefix_req[i-1]
        
        prefix_req.sort(reverse = True)
        nums.sort(reverse = True)
        res = 0
        i = 0
        while i < len(nums) and prefix_req[i] > 0:
            res += nums[i]*prefix_req[i]
            i += 1
        return res%(10**9 + 7)