class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if len(parent) == 1:
            return 1
        adj_list = defaultdict(set)
        for i, node in enumerate(parent):
            adj_list[parent[i]].add(i)
        res = []
        vis = set()
        vis.add(-1)
        def dfs(node):
            vis.add(node)
            if not adj_list[node]:
                return 1
            longest_path = 0
            second_longest_path = 0
            for child in adj_list[node]:
                longest_from_child = dfs(child)
                if s[child] != s[node]:
                    if longest_from_child > longest_path:
                        second_longest_path = longest_path
                        longest_path = longest_from_child
                    elif longest_from_child > second_longest_path:
                        second_longest_path = longest_from_child
            
            res.append(longest_path + second_longest_path + 1)
            return longest_path + 1
        _max = 1
        _max = max(_max, dfs(0))
        if res:
            return max(_max, max(res))
        else:
            return _max