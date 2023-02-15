#User function Template for python3

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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends