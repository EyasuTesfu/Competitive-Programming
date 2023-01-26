class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        _max = []
        for i in range(1, len(arr)):
            if len(_max) == 0:
                _max = [i, arr[i]]
            elif arr[i] > _max[1]:
                _max = [i, arr[i]]
                
        for i in range(len(arr[:-1])):
            if i == _max[0]:
                j = i + 1
                _max = []
                while(j < len(arr)):
                    if len(_max) == 0:
                        _max = [j, arr[j]]
                    elif arr[j] > _max[1]:
                        _max = [j, arr[j]]
                    j += 1
            res.append(_max[1])
        res.append(-1)
        return res
                