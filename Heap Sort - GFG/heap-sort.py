#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        curr = i
        cl = curr * 2 + 1
        cr = curr * 2 + 2
        
        if cl < n and arr[cl] > arr[curr]:
            curr = cl
        if cr < n and arr[cr] > arr[curr]:
            curr = cr
        
        if curr != i:
            self.swap(arr, curr, i)
            self.heapify(arr, n, curr)
        
    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            self.swap(arr, 0, i)
            self.heapify(arr, i, 0)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends