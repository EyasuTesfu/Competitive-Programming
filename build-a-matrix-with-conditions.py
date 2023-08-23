class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = {}
        row_adj = defaultdict(set)
        row_incoming = defaultdict(int)
        col = {}
        col_adj = defaultdict(set)
        col_incoming = defaultdict(int)


        for a, b in rowConditions:
            if b not in row_adj[a]:
                row_adj[a].add(b)
                row_incoming[b] += 1

        for a, b in colConditions:
            if b not in col_adj[a]:
                col_adj[a].add(b)
                col_incoming[b] += 1

        row_queue = deque()
        col_queue = deque()
        row_order = []
        col_order = []
        for i in range(1,k+1):
            if not row_incoming[i]:
                row_queue.append(i)
                row[i] = 0
            if not col_incoming[i]:
                col_queue.append(i)
                col[i] = 0
        
        while row_queue:
            node = row_queue.popleft()
            row_order.append(node)
            for neigh in row_adj[node]:
                row_incoming[neigh] -= 1
                if not row_incoming[neigh]:
                    row[neigh] = row[node] + 1
                    row_queue.append(neigh)
        
        if len(row_order) != k:
            return []
        while col_queue:
            node = col_queue.popleft()
            col_order.append(node)

            for neigh in col_adj[node]:
                col_incoming[neigh] -= 1
                if not col_incoming[neigh]:
                    col[neigh] = col[node] + 1
                    col_queue.append(neigh)
        
        if len(col_order) != k:
            return []
        
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for i, val in enumerate(row_order):
            c = col_order.index(val)
            matrix[i][c] = val
        return matrix