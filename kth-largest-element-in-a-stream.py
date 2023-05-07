class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)