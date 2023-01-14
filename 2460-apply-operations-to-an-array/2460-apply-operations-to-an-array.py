class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        zeros = 0
        res = []
        while(i < len(nums)):
            if nums[i] == 0:
                zeros += 1
                i += 1
            elif i < len(nums)-1 and nums[i] == nums[i+1]:
                res.append(nums[i]*2)
                zeros += 1
                i += 2
            else:
                res.append(nums[i])
                i += 1
        return res + [0]*zeros