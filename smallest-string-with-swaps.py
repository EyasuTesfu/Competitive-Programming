class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = {i:i for i in range(len(s))}
        self.index = {i:i for i in range(len(s))} # for later update of the indices
        self.s = s
        for i, j in pairs:
            self.union(i,j)
        # sort the letters with the same parent
        conn = defaultdict(list) # to collect all letters with the same parent
        for ind in self.parent:
            conn[self.find(ind)].append(ind)
        for child_ord in conn:
            conn[child_ord] = sorted(conn[child_ord], key = lambda x: s[x])
            sort_ind = sorted(conn[child_ord])
            for ind, let in zip(sort_ind, conn[child_ord]):
                self.index[let] = ind
        res = ["" for i in range(len(s))]
        for pos in self.index:
            res[self.index[pos]] = s[pos]
        return "".join(res)


    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return
        if self.s[rootx] > self.s[rooty]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
    def find(self, x):
        if x == self.parent[x]:
            return x
        temp = self.find(self.parent[x])
        self.parent[x] = temp
        return temp