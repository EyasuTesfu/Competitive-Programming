def insertionSort1(n, arr):
    e = arr[n - 1]
    x = n - 1
    while x > 0:
        if arr[x] < e:
            break
        x -= 1
    while e < arr[n - 2]:
        arr[n - 1] = arr[n - 2]
        print(str(arr).strip("[]").replace("'", "").replace(",", ""))
        if n - 2 > 0:
            n -= 1
        else:
            break
    if e < min(arr):
        arr[0] = e
    else:
        arr[x + 1] = e
    print(str(arr).strip("[]").replace("'", "").replace(",", ""))
