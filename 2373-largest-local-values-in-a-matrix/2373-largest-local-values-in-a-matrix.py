class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                _max  = 0
                k = i
                while(k < len(grid) and k < i + 3):
                    l = j
                    while(l < len(grid[0]) and l < j + 3):
                        _max = max(_max, grid[k][l])
                        l += 1
                    k += 1
                res[i].append(_max)
        return res