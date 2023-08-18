class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(set)
        incoming = [0]*numCourses
        for a, b in prerequisites:
            adj_list[b].add(a)
            incoming[a] += 1

        queue = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        temp_list = [set() for _ in range(numCourses)]
        while queue:
            val = queue.popleft()
            for neigh in adj_list[val]:
                incoming[neigh] -= 1
                for i in temp_list[val]:
                    temp_list[neigh].add(i)
                temp_list[neigh].add(val)
                if incoming[neigh] == 0:
                    queue.append(neigh)
        ans = []
        for a, b in queries:
            ans.append(b in temp_list[a])
        return ans