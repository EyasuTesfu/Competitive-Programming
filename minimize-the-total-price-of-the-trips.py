class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        count_trips = defaultdict(int)
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        def dfs(src, dst, path, vis):
            if src == dst:
                for p in path:
                    count_trips[p] += 1
                return
            for neigh in adj_list[src]:
                if neigh not in vis:
                    path.append(neigh)
                    vis.add(neigh)
                    dfs(neigh, dst, path[:], vis)
                    path.pop()
        

        for a, b in trips:
            vis = set()
            vis.add(a)
            dfs(a, b, [a], vis)
        
        memo = {}
        def dp(node, parent, prev_halved):
            if (node, prev_halved) in memo:
                return memo[(node, prev_halved)]
            ans1 = count_trips[node]* price[node]
            ans2 = count_trips[node] * price[node]/2
            for neigh in adj_list[node]:
                if neigh != parent:
                    ans1 += dp(neigh, node, False)
            
            if prev_halved:
                memo[(node, prev_halved)] = ans1
                return memo[(node, prev_halved)]
                          
            for neigh in adj_list[node]:
                if neigh != parent:
                    ans2 += dp(neigh, node, True)
            
            memo[(node, prev_halved)] = min(ans1, ans2)
            return memo[(node, prev_halved)]
        return int(dp(0, -1, False))