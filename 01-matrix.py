class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions =  [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque()
        res = [[float('inf') if mat[i][j] == 1 else 0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
        while queue:
            row, col, dist = queue.popleft()
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                    if mat[new_row][new_col] == 1 and res[new_row][new_col] > dist+1:
                        res[new_row][new_col] = dist + 1
                        queue.append((new_row, new_col, dist+1))
                
        return res