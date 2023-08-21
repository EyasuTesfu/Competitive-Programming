from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    adj_list = defaultdict(set)
    incoming = defaultdict(int)
    for a, b in prerequisites:
        adj_list[a].add(b)
        incoming[b] += 1
    queue = deque()
    course_taken = 0
    for i in range(1, n+1):
        if not incoming[i]:
            queue.append(i)

    count = 0
    while queue:
        count += 1
        length = len(queue)
        for i in range(length):
            course_taken += 1
            val = queue.popleft()
            for item in adj_list[val]:
                incoming[item] -= 1
                if incoming[item] == 0:
                    queue.append(item)
    if course_taken != n:
        return -1
    return count
            