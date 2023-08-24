class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # if there is a cycle then it's always false
        adj_list = defaultdict(set)
        color = {}
        for a, b in dislikes:
            adj_list[a].add(b)
            adj_list[b].add(a)
        def dfs(node):
            for neigh in adj_list[node]:
                if neigh in color:
                    if color[neigh] == color[node]:
                        return False
                else:
                    color[neigh] = 1 - color[node]
                    if not dfs(neigh):
                        return False
            return True
        
        for i in range(1, n):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True