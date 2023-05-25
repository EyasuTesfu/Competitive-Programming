class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.parent = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
        self.index = {i:source[i] for i in range(n)}
        self.child = defaultdict(set)
        self.source_val = defaultdict(int)
        # union the allowedswaps index
        for i,j in allowedSwaps:
            self.union(i,j)
        # find the childs of the parent and put them in a set and hold the count on how much they exist in each group
        for i in self.parent:
            parent = self.find(i)
            self.child[parent].add(i)
            self.source_val[(parent,source[i])] += 1
        # loop over and if the amount of a value with the same parent is different in source than in target, we add the hamming
        hamming = 0
        for i, val in enumerate(target):
            parent = self.find(i)
            if (parent, val) in self.source_val:
                self.source_val[(parent, val)] -= 1
                if not self.source_val[(parent, val)]:
                    del self.source_val[(parent, val)]
            else:
                hamming += 1
        return hamming
    
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
    def find(self, x):
        if x == self.parent[x]:
            return x
        temp = self.find(self.parent[x])
        self.parent[x] = temp
        return temp