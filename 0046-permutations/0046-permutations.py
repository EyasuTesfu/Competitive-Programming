class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bfs(arr, vis = set()):
            if len(arr) == len(nums):
                res.append(arr)
                return
            for num in nums:
                if num not in vis:
                    arr.append(num)
                    vis.add(num)
                    bfs(arr[:], vis)
                    vis.discard(num)
                    arr.pop()
        bfs([])
        return res