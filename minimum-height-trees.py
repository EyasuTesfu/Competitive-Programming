class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        
        queue = deque()
        for edge in adj_list:
            if len(adj_list[edge]) == 1:
                queue.append(edge)
        

        while queue:
            length = len(queue)
            candidate = queue.copy()
            for i in range(length):
                val = queue.popleft()
                for neighbor in adj_list[val]:
                    adj_list[neighbor].remove(val)
                    if len(adj_list[neighbor]) == 1:
                        queue.append(neighbor)
        return candidate