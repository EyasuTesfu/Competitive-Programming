class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        relate_dict = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    relate_dict[(i, "row")].add((j, "col"))
                    relate_dict[(j, "col")].add((i, "row"))
        
        vis = set()
        def dfs(node, id):
            if (node, id) in vis:
                return
            vis.add((node, id))
            for neigh in relate_dict[node, id]:
                dfs(neigh[0], neigh[1])
        count = 0
        for i in range(n):
            if (i, "row") not in vis:
                dfs(i, "row")
                count += 1
            if (i, "col") not in vis:
                dfs(i, "col")
                count += 1
        return count