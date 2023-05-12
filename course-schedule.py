class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_graph = defaultdict(set)
        incoming = [0] * numCourses
        for chl, par in prerequisites:
            adj_graph[par].add(chl)
            incoming[chl] += 1
        # look for courses that doesn't have prerequisitesd
        no_incoming = []
        colors = defaultdict(int)
        for idx, val in enumerate(incoming):
            colors[idx] = 0
            if val == 0:
                no_incoming.append(idx)
        
        # run a dfs for the values that does not have an incoming edge
        total_courses = []
        for course in no_incoming:
            if not self.dfs(course, colors, adj_graph, total_courses):
                return False
        if len(total_courses) != numCourses:
            return False
        return True
    def dfs(self, course, colors, adj_graph, total_courses):
        # if the Course is visited in a different path
        if colors[course] == 2:
            return True
        # if the Course is visited in the same path, there is a cycle
        if colors[course] == 1:
            return False

        colors[course] = 1
        # for every child in the ad
        for chl in adj_graph[course]:
            if not self.dfs(chl, colors, adj_graph, total_courses):
                return False
        # the course has been learnt in this path and moved to another branch
        colors[course] = 2
        total_courses.append(course)
        return True