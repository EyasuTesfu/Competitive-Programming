class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr
        num_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        num_rank[sorted_arr[0]] = 1
        for i in range(1, n):
            if sorted_arr[i] in num_rank:
                continue
            rank += 1
            num_rank[sorted_arr[i]] = rank

        for i in range(len(arr)):
            arr[i] = num_rank[arr[i]]
        
        return arr