# Problem: an Unsorted array with the range
# Required: To sort the integer using counting sort
# Solution: Create an zero array of 100 and increment one of the index of zero_arr to the corresponding
# array value through iterating the array from start to finish
def countingSort(arr):
    zero_arr = [0]*(100)
    i = 0
    while i < len(arr):
        zero_arr[(arr[i])] += 1
        i += 1
    return zero_arr


arr = [1, 1, 3, 2, 1]
# arr2 = [3, 2, 2, 2, 5]
# zero_arr = [0, 0, 0, 0, 0]
# returned_arr = [0, 4, 1, 0, 5]

print(countingSort(arr))
