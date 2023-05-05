class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_network = defaultdict(set)
        for edge in roads:
            road_network[edge[0]].add(edge[1])
            road_network[edge[1]].add(edge[0])
        _max = 0
        for node in road_network:
            nl = len(road_network[node])
            for neig in road_network:
                if node == neig:
                    continue
                if neig in road_network[node]:
                    _max = max((nl+ len(road_network[neig]))-1, _max)
                else:
                    _max = max((nl+ len(road_network[neig])), _max)
        return _max