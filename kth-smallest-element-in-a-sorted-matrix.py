class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            if matrix:
                heapq.heappush(heap, (matrix[i][0], i, 0))
        
        count = 0
        while heap:
            count += 1
            val, arr_idx, ele_idx = heapq.heappop(heap)
            if count == k:
                return val
            if ele_idx + 1 < len(matrix[arr_idx]):
                heapq.heappush(heap, (matrix[arr_idx][ele_idx+1], arr_idx, ele_idx + 1))