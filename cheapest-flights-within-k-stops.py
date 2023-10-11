class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def djikstra(src, dst, second):
            adj_list = defaultdict(set)
            cost_list = defaultdict(int)
            if second:
                for u, v, w in flights:
                    adj_list[v].add(u)
                    cost_list[(v,u)] = w
            else:
                for u, v, w in flights:
                    adj_list[u].add(v)
                    cost_list[(u,v)] = w

            dist = [float('inf') for _ in range(n)]
            dist[src] = 0
            
            priority_queue = [(0, src, 0)]
            vis = set()
            while priority_queue:
                cost, node, count = heapq.heappop(priority_queue)
                if node in vis or count > k:
                    continue
                
                vis.add(node)

                for next in adj_list[node]:
                    new_cost = cost + cost_list[(node, next)]
                    if new_cost < dist[next]:
                        dist[next] = new_cost
                        heapq.heappush(priority_queue, (new_cost, next, 1+count))
            return dist[dst]
        ans = min(djikstra(src, dst, False), djikstra(dst, src, True))
        if ans == float('inf'):
            return -1
        return ans