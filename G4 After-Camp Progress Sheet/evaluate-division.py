class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        to_all_path = defaultdict(dict) # holds a dictionary that has the shortest path from the node to all the available paths
        adj_list = defaultdict(set)
        direct_conn = defaultdict(int)
        valid_strings = set()
        equations2 = equations
        for i in range(len(equations)):
            adj_list[equations[i][0]].add(equations[i][1])
            direct_conn[(equations[i][0], equations[i][1])] = values[i]
            valid_strings.add(equations[i][0])
            valid_strings.add(equations[i][1])
            equations2.append([equations[i][1], equations[i][0]])
            values.append(1/values[i])

        def belman_ford(start):
            cost = {}
            for _str in valid_strings:
                cost[_str] = -1
            cost[start] = 1
            for conn in adj_list[start]:
                cost[conn] = direct_conn[(start, conn)]
            priority_queue = [(1, start)]
            
            for _ in range(len(valid_strings)-1):
                for i in range(len(equations2)):
                    if cost[equations2[i][0]] != -1 and cost[equations2[i][0]] * values[i] > cost[equations2[i][1]]:
                        cost[equations2[i][1]] = cost[equations2[i][0]] * values[i]
            
            to_all_path[start] = cost

        for node in valid_strings:
            belman_ford(node)
        
        res = []
        for a, b in queries:
            if a not in valid_strings or b not in valid_strings:
                res.append(-1)
            else:
                res.append(to_all_path[a][b])

        return res