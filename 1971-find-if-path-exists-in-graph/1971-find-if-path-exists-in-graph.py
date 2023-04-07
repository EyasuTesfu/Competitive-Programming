class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a_list = defaultdict(list)
        for i in range(len(edges)):
            a_list[edges[i][0]].append(edges[i][1])
            a_list[edges[i][1]].append(edges[i][0])
    
        def dfs(node, visited = set()):
            if node == destination:
                return True
            visited.add(node)
            for nod in a_list[node]:
                if nod not in visited:
                    found = dfs(nod, visited)
                    if found:
                        return True
        return dfs(source)
            