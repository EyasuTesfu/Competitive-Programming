class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        _min = [i]
        while i >= 0:
            if arr[i] > arr[_min[-1]]:
                idx = _min.pop()
                while _min and arr[_min[-1]] < arr[i]:
                    idx = _min.pop()
                arr[i], arr[idx] = arr[idx], arr[i]
                return arr
            elif arr[i] < arr[_min[-1]]:
                _min.append(i)
            elif arr[i] == arr[_min[-1]]:
                _min.pop()
                _min.append(i)
            i -= 1
        return arr