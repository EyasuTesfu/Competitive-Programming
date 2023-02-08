class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        for i in range(len(s)):
            last[s[i]] = i
        i = 0
        while(i < len(s)):
            if last[s[i]] == len(s)-1:
                res.append(last[s[i]]-i+1)
                return res
            if last[s[i]] - i == 0:
                res.append(1)
                i += 1
            else:
                j = i+1
                count = last[s[i]]-i+1
                _last = last[s[i]]
                while(j < _last):
                    if last[s[j]] > _last:
                        count += last[s[j]] - _last
                        _last = last[s[j]]
                    j += 1
                res.append(count)
                i = _last + 1
        return res