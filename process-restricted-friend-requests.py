class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        self.root = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
        self.not_friend = defaultdict(set) # act as friendship judgement
        self.child = defaultdict(set) # holds the child of every parent
        for a, b in restrictions:
            self.not_friend[a].add(b)
            self.not_friend[b].add(a)
        for key in self.root:
            self.child[key].add(key)
        res = []
        for a, b in requests:
            ans = self.union(a, b)
            res.append(ans)  
        return res  
    def find(self, x):
        if x == self.root[x]:
            return x
        temp = self.find(self.root[x])
        self.root[x] = temp
        return temp
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
    
        if rootx == rooty:
            return True

        for child in self.child[rootx]:
            if child in self.not_friend[rooty]:
                return False
        
        if self.rank[rootx] == self.rank[rooty]:
            self.root[rootx] = rooty
            self.rank[rooty] += 1
            self.not_friend[rooty].update(self.not_friend[rootx])
            self.child[rooty].update(self.child[rootx])
        elif self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
            self.not_friend[rootx].update(self.not_friend[rooty])
            self.child[rootx].update(self.child[rooty])
        else:
            self.root[rootx] = rooty
            self.not_friend[rooty].update(self.not_friend[rootx])
            self.child[rooty].update(self.child[rootx])
        return True