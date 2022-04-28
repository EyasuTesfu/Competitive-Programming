# User function Template for python3

from matplotlib.cbook import index_of


class Solution:
    def select(self, arr, i):
        self.SelectionSort(self, arr, i)

    def selectionSort(self, arr, n):
        for k in range(n-1):
            for j in range(k+1, n):
                if arr[k] > arr[j]:
                    arr[k], arr[j] = arr[j], arr[k]
        return arr
# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
