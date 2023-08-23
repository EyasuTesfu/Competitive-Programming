class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # initialize with root
        self.root = [i for i in range(len(isConnected))]
        self.rank = [0] * len(isConnected)

    
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    self.union(i, j)
        res = 0
        for i in range(len(self.root)):
            if i == self.root[i]:
                res += 1
        return res
    def union(self, x, y):            
        rootX = self.find(x)
        rootY = self.find(y)
        if x != y:
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootX] += 1
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
    def find(self, x):
        parent = x
        while parent != self.root[parent]:
            parent = self.root[parent]
        
        while x != parent:
            temp_parent = self.root[x]
            self.root[x] = parent
            x = temp_parent
        return parent