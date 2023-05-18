class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.weight = {}
        _min = sys.maxsize
        for p1, p2, wei in roads:
            self.union(p1-1, p2-1)
            self.weight[(p1-1, p2-1)] = wei
        val = self.find(0)
        for p1, p2, wei in roads:
            if self.find(p1-1) == val:
                _min = min(_min, self.weight[(p1-1, p2-1)])
        return _min
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
        while self.root[member] != member:
            member = self.root[member]

        while x != member:
            parent = self.root[x]
            self.root[x] = member
            x = parent
        return member