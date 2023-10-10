class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(set)
        edge_sucprob = defaultdict(int)
        for i in range(len(edges)):
            adj_list[edges[i][0]].add(edges[i][1])
            adj_list[edges[i][1]].add(edges[i][0])
            edge_sucprob[(edges[i][0], edges[i][1])] = succProb[i]
            edge_sucprob[(edges[i][1], edges[i][0])] = succProb[i]

        
        def djikstra(start, end):
            if start == end:
                return 1
            probability = [float('-inf') for _ in range(n)]
            probability[start] = 1
            priority_queue = [(1, start)]
            vis = set()

            while priority_queue:
                curr_prob, curr_node = heapq.heappop(priority_queue)

                if curr_node in vis:
                    continue
                
                vis.add(curr_node)
                for neigh in adj_list[curr_node]:
                    prob = abs(curr_prob * edge_sucprob[(neigh, curr_node)])
                    if prob >= probability[neigh]:
                        probability[neigh] = prob
                        heapq.heappush(priority_queue, (-prob, neigh))
    
            if probability[end] == float('-inf'):
                return 0
            return probability[end]
        return djikstra(start_node, end_node)