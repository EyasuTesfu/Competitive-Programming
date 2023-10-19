class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.rank[0] = float('inf')
        self.root[firstPerson] = 0
        sorted_meetings = sorted(meetings, key = lambda x: x[2])
        i = 0
        while i < len(sorted_meetings):
            j = i
            while j < len(sorted_meetings)-1:
                if sorted_meetings[j][2] != sorted_meetings[j+1][2]:
                    break
                j += 1
            for k in range(i, j+1):
                self.union(sorted_meetings[k][0], sorted_meetings[k][1])          
                    
            for k in range(i, j+1):
                if self.find(sorted_meetings[k][0]) != 0:
                    self.root[sorted_meetings[k][0]] = sorted_meetings[k][0]
                if self.find(sorted_meetings[k][1]) != 0:
                    self.root[sorted_meetings[k][1]] = sorted_meetings[k][1]
            i = j + 1
        res = []
        for i in range(n):
            if self.root[i] == 0 or self.root[i] == firstPerson:
                res.append(i)
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