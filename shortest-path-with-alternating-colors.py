class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_edges = defaultdict(list)
        blue_edges = defaultdict(list)
        for edges in redEdges:
            red_edges[edges[0]].append(edges[1])
        for edges in blueEdges:
            blue_edges[edges[0]].append(edges[1])
        res = [-1 for i in range(n)]
        # do bfs on the redEdges
        queue = deque()
        queue.append((0,0,-1))
        vis = set()
        vis.add((0,-1))
        while queue:
            node, dist, color = queue.popleft()
            if res[node] == -1:
                res[node] = dist
            
            if color != 0:
                for ver in red_edges[node]:
                    if (ver, 0) not in vis:
                        vis.add((ver, 0))
                        queue.append((ver, dist+1, 0))
            if color != 1:
                for ver in blue_edges[node]:
                    if (ver, 1) not in vis:
                        vis.add((ver, 1))
                        queue.append((ver, dist+1, 1))
        return res