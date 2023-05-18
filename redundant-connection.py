class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.root = [i for i in range(len(edges))]
        self.rank = [1 for i in range(len(edges))]
        res = []
        for n1, n2 in edges:
            if self.find(n1-1) != self.find(n2-1):
                self.union(n1-1, n2-1)
            else:
                res = [n1, n2]
        return res
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