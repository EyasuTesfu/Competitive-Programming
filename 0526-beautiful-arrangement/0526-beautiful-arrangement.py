class Solution:
    def countArrangement(self, n: int) -> int:
        res = []
        nums = [i for i in range(1,n+1)]
        def bfs(arr, vis = 0):
            if len(arr) == len(nums):
                res.append(arr)
                return
            for i in range(len(nums)):
                if not (vis & (1 << i)):
                    if nums[i] % (len(arr)+1) == 0 or (len(arr) + 1) % nums[i] == 0:
                        arr.append(nums[i])
                        vis = vis | (1 << (i))
                        bfs(arr[:], vis)
                        vis = vis ^(1 << (i))
                        arr.pop()
        bfs([])
        return len(res)