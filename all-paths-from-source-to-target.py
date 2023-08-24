class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return
            for neigh in graph[node]:
                dfs(neigh, path + [neigh])
        dfs(0, [0])
        return res