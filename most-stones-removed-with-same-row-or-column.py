class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.size = {(pos[0],pos[1]): 1 for pos in stones}
        self.root = {(pos[0],pos[1]):(pos[0],pos[1]) for pos in stones}

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))
        count = 0
        for parent in self.root:
            if parent == self.root[parent]:
                if self.size[parent] > 1:
                    count += self.size[parent] - 1
        
        return count


    def union(self, p1, p2):
        loc1 = self.find(p1)
        loc2 = self.find(p2)

        if loc1 != loc2:
            if self.size[loc1] < self.size[loc2]:
                self.root[loc1] = loc2
                self.size[loc2] += self.size[loc1]
            elif self.size[loc1] == self.size[loc2]:
                self.root[loc2] = loc1
                self.size[loc1] += self.size[loc2]
            else:
                self.root[loc2] = loc1
                self.size[loc1] += self.size[loc2]
    
    def find(self, p):
        member = p
        while p != self.root[p]:
            p = self.root[p]
        
        while member != p:
            parent = self.root[member]
            self.root[member] = p
            member = parent
        return p