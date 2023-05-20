class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.root = {i:i for i in range(len(accounts))}
        self.parent = defaultdict(set)
        name_number = {i:accounts[i][0] for i in range(len(accounts))}
        for j in range(len(accounts)):
            for i in range(len(accounts[j])):
                if i == 0:
                    continue
                    # self.root[accounts[j][i]+str(j)] = j
                else:
                    if accounts[j][i] in self.root:
                        self.union(j, self.root[accounts[j][i]])
                    self.root[accounts[j][i]] = j
        res = []
        for email in self.root:
            if self.root[email] == email:
                continue
            else:
                if type(email) != int:
                    self.parent[self.find(email)].add(email)
        for num in self.parent:
            res.append([name_number[num]] + sorted(self.parent[num]))
        return res
    def union(self, x, y):
        nameX = self.find(x)
        nameY = self.find(y)

        if nameX != nameY:
            self.root[nameX] = nameY
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x