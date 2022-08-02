'''
Question link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
Solution: Use a recursive function to find the answer, but you can also use a queue based approach
which would involve deleting and appending based on the size of k'''


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def findTheRealWinner(n, k) -> int:
            if n == 1:
                return 0
            else:
                return (findTheRealWinner(n-1, k) + k) % n
        return findTheRealWinner(n, k)+1
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         queue = [i for i in range(n, 0, -1)]
#         while(n > 1):
#             for _ in range(k-1):
#                 popped = queue.pop()
#                 queue.insert(0, popped)
#             queue.pop()
#             n-=1
#         return queue[0]
