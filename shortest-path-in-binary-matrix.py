class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1 if not grid[0][0] else -1
        
        if grid[0][0] or grid[m - 1][n - 1]:
            return -1
        
        directions = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
        q = collections.deque([(0, 0, 1)])
        
        while q:
            i, j, pathLength = q.popleft()
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                if newI == m - 1 and newJ == n - 1:
                    return pathLength + 1
                
                if newI == -1 or newI == m or newJ == -1 or newJ == n or grid[newI][newJ]:
                    continue
                
                grid[newI][newJ] = 1
                q.append((newI, newJ, pathLength + 1))
        
        return -1