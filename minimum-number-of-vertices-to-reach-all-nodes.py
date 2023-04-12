class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # add the source to a set, remove the destination from the set if it exists
        res = set()
        dest = set()
        for s, d in edges:
            dest.add(d)
        for s,d in edges:
            if s not in dest:
                res.add(s)
        return res