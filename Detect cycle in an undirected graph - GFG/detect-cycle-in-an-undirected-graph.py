from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def has_cycle(vis, vertex, parent):
	        vis.add(vertex)
	        for neighbour in adj[vertex]:
	            if neighbour == parent:
	                continue
	            if neighbour in vis:
	                return True
	            if has_cycle(vis, neighbour, vertex):
	                return True
	        return False
	    vis = set()
	    vis.add(-1)
	    for i in range(V):
	        if i not in vis:
	            if has_cycle(vis, i, -1):
	                return True
	    return False
	    
	       
	   
	    

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends