class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # add prefix_sum
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        # find the shortest subarray
        queue = deque() # holds the minimum prefix_sum than the one we're looking at
        queue.append(0)
        length = n+1
        # left = 0
        for right in range(1,n+1):
            # going forward and checking if we found the sum that suits condition
            while queue and prefix[right] - prefix[queue[0]] >= k:
                length = min(length, right-queue[0])
                queue.popleft()
            # popping middle values and even the queue[0] so that we can jump to the next small prefix that won't make prefix[right] - prefix[queue[0]] negative
            while queue and prefix[right] < prefix[queue[-1]]:
                queue.pop()
            queue.append(right)
        if length == n+1: return -1
        return length