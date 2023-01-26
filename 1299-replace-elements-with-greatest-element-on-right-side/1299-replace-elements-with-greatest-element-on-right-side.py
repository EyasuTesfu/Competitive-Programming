class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        _max = -1
        for i in range(-1, -len(arr), -1):
            _max = max(arr[i], _max)
            res.append(_max)
        res.reverse()
        res.append(-1)
        return res
                       
            