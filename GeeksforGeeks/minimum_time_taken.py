from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        adj_list = defaultdict(set)
        prior_done = defaultdict(set)
        for a, b in edges:
            adj_list[b].add(a)
            prior_done[a].add(b)
        queue = deque()
        for i in range(1, n+1):
            if i not in adj_list:
                queue.append(i)
        count = 0
        ans = [0]*n
        while queue:
            count += 1
            length = len(queue)
            for i in range(length):
                val = queue.popleft()
                ans[val-1] = count
                for neighbor in prior_done[val]:
                    adj_list[neighbor].remove(val)
                    if len(adj_list[neighbor]) == 0:
                        queue.append(neighbor)
        return ans
                
        
        
        

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends