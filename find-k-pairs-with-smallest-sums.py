class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapq.heappush(heap, (nums1[0]+ nums2[0], 0,0))
        res= []
        while heap and k > 0:
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if i+1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res