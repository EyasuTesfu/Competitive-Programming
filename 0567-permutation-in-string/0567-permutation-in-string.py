class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        sorted_s1 = sorted(s1)
        queue = deque()
        for i in range(len(s2)):
            queue.append(s2[i])
            if len(queue) == len(s1):
                if sorted_s1 == sorted(queue):
                    return True
                queue.popleft()
        return False


            