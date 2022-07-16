'''
Question link:https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
Solution: By using a monotonic queue we are always keeping track of the smallest and
the largest element in the top of the queue as we move to the right
So when we find a larger element than the previous largest or a smaller element than the
previous smallest we check the absolute difference
[8, 2, 4, 7] 4
0
6
2, max is 2
5 then back to 3, max is 2 so no difference
I still can't think of why sliding to the next smallest if we find a greatest and jumping to the
next largest if we find a smallest when we move to the right doesn't bring a good and optimal
solution
'''


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        small_queue = []
        large_queue = []
        right = 0
        left = 0
        largest = nums[0]
        smallest = nums[0]
        lon_con_subarray = 0
        while(right < len(nums)):
            while small_queue and nums[small_queue[-1]] >= nums[right]:
                small_queue.pop()
            small_queue.append(right)
            while large_queue and nums[large_queue[-1]] <= nums[right]:
                large_queue.pop()
            large_queue.append(right)
            # print(large_queue, "large queue")
            # print(small_queue, "small queue")
            if nums[large_queue[0]] - nums[small_queue[0]] > limit:
                # if nums[right] == nums[large_queue[0]]:
                #     left = small_queue[0] + 1
                #     small_queue.pop(0)
                #     if left > large_queue[0]:
                #         large_queue.pop(0)
                # if nums[right] == nums[small_queue[0]]:
                #     left = large_queue[0] + 1
                #     large_queue.pop(0)
                #     if left > small_queue[0]:
                #         small_queue.pop(0)
                left += 1
                if left > large_queue[0]:
                    large_queue.pop(0)
                if left > small_queue[0]:
                    small_queue.pop(0)
            else:
                lon_con_subarray = max(lon_con_subarray, (right - left)+1)
                right += 1
        return lon_con_subarray
