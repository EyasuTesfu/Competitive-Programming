class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        group_precedence = defaultdict(list)
        item_precedence = defaultdict(list)
        group_incoming = defaultdict(int)
        item_incoming = defaultdict(int)

        for prev in range(n):

            for fut in beforeItems[prev]:
                if group[prev] != group[fut]:
                    group_precedence[group[fut]].append(group[prev])
                    group_incoming[group[prev]] += 1
                else:
                    item_precedence[fut].append(prev)
                    item_incoming[prev] += 1
        
        top_sort_items = []
        item_queue = deque()
        for i in range(n):
            if not item_incoming[i]:
                item_queue.append(i)
        
        while item_queue:
            node = item_queue.popleft()
            top_sort_items.append(node)
            for neigh in item_precedence[node]:
                item_incoming[neigh] -= 1
                if item_incoming[neigh] == 0:
                    item_queue.append(neigh)
        if len(top_sort_items) != n:
            return []
        
        top_sort_groups = []
        group_queue = deque()
        for i in range(group_id):
            if not group_incoming[i]:
                group_queue.append(i)
        
        while group_queue:
            node = group_queue.popleft()
            top_sort_groups.append(node)
            for neigh in group_precedence[node]:
                group_incoming[neigh] -= 1
                if group_incoming[neigh] == 0:
                    group_queue.append(neigh)
        if len(top_sort_groups) != group_id:
            return []


        adj_dict = {}
        for gr in top_sort_groups:
            adj_dict[gr] = []
        
        for item in top_sort_items:
            adj_dict[group[item]].append(item)
        
        res = []
        for group in adj_dict:
            res.extend(adj_dict[group])
        return res