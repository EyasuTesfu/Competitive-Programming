class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.parent = [i for i in range(len(strs))]
        self.rank = [0 for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                a = 0
                b = 0
                # two pointers
                while a < len(strs[i]) and b < len(strs[j]):
                    if strs[i][a] == strs[j][b]:
                        a += 1
                        b += 1
                    else:
                        break
                if a == len(strs[i]) and b == len(strs[j]):
                    self.union(i, j)
                l = a+1
                k = b+1
                while l < len(strs[i]) and k < len(strs[j]):
                    if strs[i][l] == strs[j][k]:
                        l += 1
                        k += 1
                    else:
                        if strs[i][a] == strs[j][k] and strs[j][b] == strs[i][l]:
                            if strs[i][l+1:] == strs[j][k+1:]:
                                self.union(i, j)
                        break
        res = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                res += 1
        return res


    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]