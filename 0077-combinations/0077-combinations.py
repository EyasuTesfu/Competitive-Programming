class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        values = [i for i in range(n+1)]
        res = []
        def backtracker(arr, idx):
            if len(arr) == k:
                res.append(arr)
                return
            for i in range(idx, n+1):
                backtracker(arr + [values[i]], i+1)
        backtracker([] ,1)
        return res