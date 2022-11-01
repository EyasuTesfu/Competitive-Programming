class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        prefix_dict = {}
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == k:
                count += 1
            if prefix_dict.get(prefix_sum-k, "x") != "x":
                count += prefix_dict[prefix_sum - k]

            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1
        # print(prefix_dict)
        # print(nums)
        return count
