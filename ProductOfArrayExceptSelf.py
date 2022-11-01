class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]
        prefix_mul = nums[0]
        for i in range(1, len(nums)):
            output.append(prefix_mul)
            prefix_mul *= nums[i]
        prefix_mul = nums[-1]
        # print(output)
        for i in range(len(nums)-2, -1, -1):
            if i == 0:
                output[i] = prefix_mul
            else:
                output[i] *= prefix_mul
                prefix_mul *= nums[i]
        return output
