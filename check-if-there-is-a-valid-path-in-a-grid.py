class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid[0])
        n = len(grid)
        self.root = defaultdict(tuple)
        self.rank = defaultdict(int)
        for i in range(n):
            for j in range(m):
                self.root[(i,j)] = (i,j)
                self.rank[(i,j)] = 1

        path_meaning = {1: [(0,1), (0,-1)], 2: [(1,0), (-1, 0)], 3: [(0,-1), (1,0)], 4:[(0,1),(1,0)], 5:[(-1,0), (0,-1)], 6: [(-1, 0), (0,1)]}
        connections = defaultdict(set)

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m
        for row in range(n):
            for col in range(m):
                for conn in path_meaning[grid[row][col]]:
                    conn_row = row + conn[0]
                    conn_col = col + conn[1]
                    if is_valid(conn_row, conn_col):
                        connections[(row,col)].add((conn_row, conn_col))
        for row in range(n):
            for col in range(m):
                if (row, col) in connections:
                    for nei in connections[(row,col)]:
                        for val in connections[nei]:
                            if (row, col) == val:
                                self.union((row,col),(nei))
        return self.find((0,0)) == self.find((n-1,m-1))
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    def find(self, member):
        x = member
        while member != self.root[member]:
            member = self.root[member]
        
        while x != member:
            parent = self.root[x]
            self.root[x] = member
            x = parent
        return member