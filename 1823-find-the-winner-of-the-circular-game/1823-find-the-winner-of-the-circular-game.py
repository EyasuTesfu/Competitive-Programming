class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i for i in range(n, 0, -1)]
        while(n > 1):
            for _ in range(k-1):
                popped = queue.pop()
                queue.insert(0, popped)
            queue.pop()
            n-=1
        return queue[0]
            