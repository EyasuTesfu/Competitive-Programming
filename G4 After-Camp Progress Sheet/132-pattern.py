class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_value = nums[0]
        for i in range(1, len(nums)):
            if stack:
                while stack and stack[-1][0] <= nums[i]:
                    stack.pop()
                if stack and stack[-1][1] < nums[i]:
                    return True
            stack.append([nums[i], min_value])
            min_value = min(nums[i], min_value)
        return False

