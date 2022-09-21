class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        pos = deque([0])
        for i in range(1, len(nums)):
            while pos[0] < i-k:
                pos.popleft()
            nums[i] = nums[pos[0]] + nums[i]
            while pos and nums[pos[-1]] < nums[i]:
                pos.pop()
            pos.append(i)
        return nums[-1]
