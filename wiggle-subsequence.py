class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # using backtracking
        # using dp
        up = defaultdict(int)
        down = defaultdict(int)
        up[0] = 1
        down[0] = 1
        for i in range(1,len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return max(max(down.values()), max(up.values()))