class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        queue = deque()
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                queue.append(right)
                k -= 1
            if k == 0:
                ans += (queue[0] - left + 1) * 1
            elif k == -1:
                left = queue.popleft() + 1
                ans += (queue[0] - left + 1) * 1
                k += 1
        return ans