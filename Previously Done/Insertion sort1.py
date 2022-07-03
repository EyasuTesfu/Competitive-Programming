def insertionSort1(n, arr):
    temp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = temp
        print(str(arr).strip("[]").replace(",", ""))
