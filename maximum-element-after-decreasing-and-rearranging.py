class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        arr = sorted(arr)
        _max = 0
        if arr[0] != 1:
            arr[0] = 1
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
            _max = max(arr[i], _max)
        return _max