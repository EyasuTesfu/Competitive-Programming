class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.root = {}
        for w1, w2 in zip(s1, s2):
            self.root[w1] = w1
            self.root[w2] = w2
        for w1, w2 in zip(s1, s2):
            self.union(w1, w2)
        res = []
        for let in baseStr:
            if let not in self.root:
                res.append(let)
            else:
                res.append(self.find(let))
        return "".join(res)

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
    
    def find(self, x):
        member = x
        while x != self.root[x]:
            x = self.root[x]
        
        while member != x:
            parent = self.root[member]
            self.root[member] = x
            member = parent
        return x