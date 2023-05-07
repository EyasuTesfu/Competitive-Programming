class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_words = Counter(words)
        max_heap = []
        for word in freq_words:
            heapq.heappush(max_heap, (-freq_words[word], word))
        res = [heapq.heappop(max_heap)[1] for _ in range(k)]
        return res