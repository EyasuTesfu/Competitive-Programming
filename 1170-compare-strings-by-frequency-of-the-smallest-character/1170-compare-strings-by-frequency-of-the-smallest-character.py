class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 1st part
        for i in range(len(queries)):
            queries[i] = self.frequency(queries[i])
        for i in range(len(words)):
            words[i] = self.frequency(words[i])
        words.sort()
        res = []
        for query in queries:
            res.append(self.binary_search(words, query))
        return res
        
        
    def frequency(self,letters):
        
        _counter = Counter(letters)
        freq = sorted(_counter.items(),key=lambda x:x[0])[0][1]
        
        return freq
        
    def binary_search(self,words, query_freq):
        l = 0
        r = len(words)-1
        n = len(words)
        while l <= r:
            mid = l + (r-l)//2
            if words[mid] > query_freq:
                r = mid - 1 
            else:
                l = mid + 1
        return n-l