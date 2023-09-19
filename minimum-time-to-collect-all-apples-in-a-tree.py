class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        vis = set()
        def dfs(node):
            vis.add(node)
            if not adj_list[node]:
                return 0
            count = 0
            for child in adj_list[node]:
                if child not in vis:
                    temp_val = dfs(child)
                    if hasApple[child] or temp_val:
                        count += 2 + temp_val
            return count
            
        return dfs(0)