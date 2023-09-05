class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(set)
        label_node = defaultdict(set)
        res = [1 for i in range(n)]

        for i in range(len(labels)):
            label_node[labels[i]].add(i)

        for a, b in edges:
            if a != 0:
                adj_list[a].add(b)
                adj_list[b].add(a)
            else:
                adj_list[a].add(b)

        vis = set()
        def dfs(node):
            vis.add(node)
            if not adj_list[node]:
                temp_dict = {}
                temp_dict[labels[node]] = 1
                return temp_dict
            holder = defaultdict(int)
            for child in adj_list[node]:
                if child not in vis:
                    temp_val = dfs(child)
                    for val in temp_val:
                        holder[val] += temp_val[val]
            holder[labels[node]] += 1
            res[node] = holder[labels[node]]
            return holder
            
        dfs(0)
        return res