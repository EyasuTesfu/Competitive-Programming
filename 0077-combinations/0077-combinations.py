class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        values = [i for i in range(n+1)]
        res = []
        def backtracker(arr, idx, slot_index):
            if slot_index == k:
                res.append(arr[:])
                return
            for i in range(idx, n+1):
                arr[slot_index] = i
                backtracker(arr, i+1, slot_index+1)
        backtracker([0]*k ,1, 0)
        return res