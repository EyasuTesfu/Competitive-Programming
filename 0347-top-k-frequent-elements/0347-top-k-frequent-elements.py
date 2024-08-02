class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = Counter(nums)
        heap = []
        for num in amount:
            heapq.heappush(heap, (-amount[num], num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res