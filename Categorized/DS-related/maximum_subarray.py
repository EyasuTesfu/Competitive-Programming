# problem link : https://leetcode.com/problems/maximum-subarray/description/
# ---------------------Kadane's Algorithm------------
# time complextiy O(n),
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = 0
        max_so_far = -sys.maxsize
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if nums[i] > max_ending_here:
                max_ending_here = nums[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
        return max_so_far
# -----------------------Divide and Conquer-----------------
# time complexity O(n), it's space complexity is better than Kandane's Algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        mid = (len(nums))//2
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])
        cross = self.maxCrossSubArray(nums, mid)
        return max(left, right, cross)

    def maxCrossSubArray(self, nums, mid):
        count = 0
        max_sub_left = max_sub_right = -sys.maxsize
        for i in range(mid-1, -1, -1):
            count += nums[i]
            max_sub_left = max(max_sub_left, count)
        count = 0
        for i in range(mid, len(nums)):
            count += nums[i]
            max_sub_right = max(max_sub_right, count)
        return max_sub_left + max_sub_right
