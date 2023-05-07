class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                heapq.heappush(stones, -(abs(s1-s2)))
        if stones:
            return -stones[0]
        return 0