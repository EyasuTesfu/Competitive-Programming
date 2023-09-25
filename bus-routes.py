class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # (bus, bus_count)
        def bfs():
            queue = deque()
            pos_to_bus = defaultdict(set)
            vis = set() # do not go back into a visited bus
            for i in range(len(routes)):
                for stop in routes[i]:
                    pos_to_bus[stop].add(i)
            
            if source not in pos_to_bus:
                return -1
            
            if source == target:
                return 0

            for buses in pos_to_bus[source]:
                queue.append((buses, 0))
                vis.add(buses)
            while queue:
                bus, bus_count = queue.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return bus_count + 1
                    for buses in pos_to_bus[stop]:
                        if buses not in vis:
                            queue.append((buses, bus_count+1))
                            vis.add(buses)
            return -1
        return bfs()