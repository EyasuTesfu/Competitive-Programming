from collections import defaultdict


class Graph:
    def __init__(self):
        self.list = defaultdict(list)

    def addEdge(self, u, v):
        self.list[u].append(v)
        self.list[v].append(u)

    def vertex(self, u):
        if len(self.list[u]) != 0:
            print(str(self.list[u]).replace(",", "").strip("[]"))
        else:
            print()


graph = Graph()
vertices = int(input())
oper = int(input())
for i in range(oper):
    req = list(map(int, input().split()))
    if req[0] == 1:
        graph.addEdge(req[1], req[2])
    else:
        graph.vertex(req[1])