class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for i in range(len(bombs)):
            xi, yi, ri = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                dist = math.sqrt((abs(xi-xj)**2 + abs(yi-yj)**2))
                if dist <= ri:
                    adj_list[i].add(j)
        max_bombs_exploded = 1
        def dfs(i, vis):
            vis.add(i)
            if not adj_list[i]:
                return 0
            res = 0
            for j in adj_list[i]:
                if j not in vis:
                    res += 1 + dfs(j, vis)
            return res
        for i in range(len(bombs)):
            vis = set()
            max_bombs_exploded = max(max_bombs_exploded, 1+dfs(i, vis))
        return max_bombs_exploded