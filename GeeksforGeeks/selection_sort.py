class Solution: 
    def select(self, arr, i):
        _min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[_min]:
                _min = j
        arr[i] , arr[_min] = arr[_min], arr[i]
                
                
    def selectionSort(self, arr,n):
        for i in range(n-1):
            self.select(arr, i)
        return arr