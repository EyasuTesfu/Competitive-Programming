class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = _max
            _max = max(temp, _max)
        return arr