class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.weight = {}
        self.parent = {(i,j):(i,j) for i,j in points}
        self.rank = {(i,j): 0 for i,j in points}
        self.res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                self.weight[((points[i][0], points[i][1]), (points[j][0], points[j][1]))] = dist
        min_distes = sorted(self.weight, key = lambda x: self.weight[x])
        for u, v in min_distes:
            self.union(u,v)
        return self.res



    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rooty] += 1
        self.res += self.weight[(x,y)]
    def find(self, x):
        if x == self.parent[x]:
            return x
        temp = self.find(self.parent[x])
        self.parent[x] = temp
        return temp