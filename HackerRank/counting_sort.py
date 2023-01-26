def countingSort(arr):
    counter = [0 for i in range(100)]
    for num in arr:
        counter[num] += 1
    return counter
