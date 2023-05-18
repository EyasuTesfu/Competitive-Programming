class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.root = {}
        let = set()
        for equ in equations:
            if equ[0] not in let:
                let.add(equ[0])
                self.root[equ[0]] = equ[0]
            if equ[-1] not in let:
                let.add(equ[-1])
                self.root[equ[-1]] = equ[-1]
            if equ[1:3] == "==":
                self.union(equ[0],equ[-1])
        for equ in equations:
            if equ[1:3] == "!=":
                if self.find(equ[0]) == self.find(equ[-1]):
                        return False
        return True

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