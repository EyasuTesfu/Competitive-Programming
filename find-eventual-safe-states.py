class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_graph = defaultdict(list)
        outgoing = [0] * len(graph)
        terminal_nodes = []

        # key == child, values == parents
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj_graph[graph[i][j]].append(i)
                outgoing[i] += 1

        # identify the terminal_nodes
        res = []
        queue = deque()
        for idx, val in enumerate(outgoing):
            if val == 0:
                terminal_nodes.append(idx)
                queue.append(idx)

        # implement a BFS starting from the terminal nodes and check their outgoing value by decreasing it, if it becomes zero then it's guaranteed that they lead to the terminal node
        while queue:
            safe = queue.popleft()
            res.append(safe)
            for ingoing in adj_graph[safe]:
                outgoing[ingoing] -= 1
                if outgoing[ingoing] == 0:
                    queue.append(ingoing)
        return sorted(res)