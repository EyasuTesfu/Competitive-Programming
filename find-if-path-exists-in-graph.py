class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        for node1, node2 in edges:
            self.union(node1, node2)
        return self.find(source) == self.find(destination)
        
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
        if self.root[member] == member:
            return member
        return self.find(self.root[member])