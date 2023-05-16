class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestor = defaultdict(list)
        for i in range(len(edges)):
            ancestor[edges[i][1]].append(edges[i][0])
        res = []
        print(ancestor)
        for i in range(n):
            if not ancestor[i]:
                res.append([])
            else:
                anc_list = []
                queue = deque()
                vis = set()
                for anc in ancestor[i]:
                    queue.append(anc)
                    vis.add(anc)
                while queue:
                    anc = queue.popleft()
                    anc_list.append(anc)
                    for par in ancestor[anc]:
                        if par not in vis:
                            queue.append(par)
                            vis.add(par)
                res.append(sorted(anc_list))
        return res