class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adj_list = defaultdict(list)
        incoming = defaultdict(set)
        for i in range(len(edges)):
            if edges[i] != -1:
                adj_list[i].append(edges[i])
                incoming[edges[i]].add(i)

        queue = deque()
        vis = set()
        for i in range(len(edges)):
            if not incoming[i]:
                queue.append(i)
        top_sort_order = []
        while queue:
            node = queue.popleft()
            top_sort_order.append(node)
            for neigh in adj_list[node]:
                incoming[neigh].remove(node)
                if not incoming[neigh]:
                    queue.append(neigh)
        vis = set()
        for i in range(len(edges)):
            if not incoming[i]:
                vis.add(i)
        queue = deque()
        max_cycle = 0
        for i in range(len(edges)):
            if i not in vis:
                queue.append([i, 1])

            while queue:
                node, count = queue.popleft()
                vis.add(node)
                for neigh in adj_list[node]:
                    if neigh not in vis:
                        queue.append([neigh, count+1])
                    else:
                        max_cycle = max(max_cycle, count)
        if not max_cycle:
            return -1
        return max_cycle