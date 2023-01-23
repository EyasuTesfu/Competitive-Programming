class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        down = False
        up = False
        for i in range(1, len(arr)):
            if up == False and arr[i-1] > arr[i]:
                return False
            if arr[i-1] == arr[i]:
                return False
            if up == False and arr[i-1] < arr[i]:
                up = True
            elif up == True:
                if arr[i-1] > arr[i]:
                    down = True
                    j = i
                    while(j < len(arr) and arr[j-1] > arr[j]):
                        j += 1
            if down == True:
                if j == len(arr):
                    return True
                else:
                    return False
        return False