class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        def bfs(arr, vis = 0):
            if arr == n:
                self.res += 1
                return
            for i in range(1,n+1):
                if not (vis & (1 << i)):
                    if i % (arr+1) == 0 or (arr + 1) % i == 0:
                        arr += 1
                        vis = vis | (1 << (i))
                        bfs(arr, vis)
                        vis = vis ^(1 << (i))
                        arr -= 1
        bfs(0)
        return self.res