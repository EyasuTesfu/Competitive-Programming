class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)
        for a, b in adjacentPairs:
            adj_list[a].add(b)
            adj_list[b].add(a)
        
        starter_node = 0
        print(adj_list)
        for node in adj_list:
            if len(adj_list[node]) == 1:
                starter_node = node
                break
        
        answer = []
        queue = deque()
        queue.append(starter_node)
        print(queue)
        while queue:
            val = queue.popleft()
            answer.append(val)
            print(val)
            for item in adj_list[val]:
                adj_list[item].remove(val)
                queue.append(item)
        return answer