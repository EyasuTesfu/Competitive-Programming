class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        if count == k:
            return i
        pos = 0
        i = 1
        while i < 2001:
            if pos < len(arr):
                if i < arr[pos]:
                    count += 1
                    if count == k:
                        return i
                if i == arr[pos]:
                    pos += 1
            else:
                count += 1
                if count == k:
                    return i
            i += 1
        
        

            