class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [nums[-1]]
        nums = nums + nums
        res = [-1]
        for i in range(len(nums)-2, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(nums[i])
        return res[::-1][:len(res)//2]