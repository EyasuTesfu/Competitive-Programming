class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if mid -1 < 0:
                return mid + 1
            elif mid + 1 >= len(arr):
                return mid-1
            
            elif arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid+1
            
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid-1

        return mid