class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.root = {(i,j):(i,j) for i in range(row) for j in range(col)}
        self.rank = {(i,j):0 for i in range(row) for j in range(col)}
        self.grid = [[0]* col for _ in range(row)]
        self.root["left"] = "left"
        self.rank["left"] = 0
        self.root["right"] = "right"
        self.rank["right"] = 0
        # u, d, l, r, ul, ur, dl, dr
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

        def is_valid(r, c):
            return 0 <= r < row and 0 <= c < col
        for idx, val in enumerate(cells):
            _row = val[0]-1
            _col = val[1]-1
            self.grid[_row][_col] = 1
            if _col == 0:
                self.union((_row, _col), "left")
            if _col == col-1:
                self.union((_row, _col), "right")
            for r, c in directions:
                new_r = _row + r
                new_c = _col + c
                if is_valid(new_r, new_c) and self.grid[new_r][new_c] == 1:
                    self.union((_row,_col),(new_r, new_c))
                    
                if self.find("left") == self.find("right"):
                    return idx
                             
        return len(cells)-1

    def union(self, p1, p2):
        loc1 = self.find(p1)
        loc2 = self.find(p2)

        if loc1 != loc2:
            if self.rank[loc1] > self.rank[loc2]:
                self.root[loc2] = loc1

            
            elif self.rank[loc2] > self.rank[loc1]:
                self.root[loc1] = loc2
            
            else:
                self.root[loc1] = loc2
                self.rank[loc2] += 1
    
    def find(self, p):
        member = p
        while p != self.root[p]:
            p = self.root[p]
        
        while member != p:
            parent = self.root[member]
            self.root[member] = p
            member = parent
        return p