'''
Problem link = https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
This type of shortest sub array involves a -ve number, that's why we use deque to both slide when we get to the target
when we fall below our previous sum we pop every element that's before the new sum to continue the monotonic, and we pop only 
the gains
Solution steps involve the concept of sliding window + using a deque to use as a way to continue the monotonically increasing
structure and sliding over the deque until we fall under the target, and updating the shortest sub array
'''


from collections import deque
import sys
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        _sum = 0
        dq = deque()
        short_arr = sys.maxsize
        n = len(nums)
        for i in range(n):
            _sum += nums[i]
            if _sum >= k:
                short_arr = min(short_arr, i+1)
            index = sys.maxsize
            while(dq and ((_sum - dq[0][1]) >= k)):
                index = dq[0][0]
                dq.popleft()
            if index != sys.maxsize:
                short_arr = min(i - index, short_arr)
            while(dq and _sum < dq[-1][1]):
                dq.pop()
            dq.append([i, _sum])
        if short_arr > n:
            return -1
        return short_arr
