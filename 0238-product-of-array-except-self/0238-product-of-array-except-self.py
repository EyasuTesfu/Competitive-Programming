class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # an excluded prefix_mul
        # 1, 1, 2, 6
        # 1, 4, 12, 24
        # 24, 12, 4, 1
        prefix_1 = [1]
        prefix_2 = [1]
        mul = 1
        res = []
        for i in range(1,len(nums)):
            mul *= nums[i-1]
            prefix_1.append(mul)
        mul = 1
        for i in range(len(nums)-2, -1, -1):
            mul *= nums[i+1]
            prefix_2.append(mul)
        l, r = 0, len(nums)-1
        while l < len(nums) and r >= 0:
            res.append(prefix_1[l]*prefix_2[r])
            l += 1
            r -= 1
        return res