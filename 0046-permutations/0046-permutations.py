class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bfs(arr, vis = 0):
            if len(arr) == len(nums):
                res.append(arr)
                return
            for i in range(len(nums)):
                if not (vis & (1 << i)):
                    arr.append(nums[i])
                    vis = vis | (1 << (i))
                    bfs(arr[:], vis)
                    vis = vis ^(1 << (i))
                    arr.pop()
        bfs([])
        return res