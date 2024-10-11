class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        nums_ind = [(nums[i], i) for i in range(len(nums))]
        nums_ind.sort()
        min_ind = nums_ind[0][1]
        res = 0
        for val, ind in nums_ind:
            res = max(res, ind - min_ind)
            min_ind = min(min_ind, ind)
        return res
            
            

            
                

