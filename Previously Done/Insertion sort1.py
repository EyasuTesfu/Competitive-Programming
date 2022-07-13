

def insertionSort1(n, arr):
    i = -2
    temp = arr[-1]
    while(i >= -n):
        if arr[i] > temp:
            arr[i+1] = arr[i]
            print(str(arr).strip("[]").replace(",", ""))
            if arr[i] == arr[0]:
                arr[i] = temp
                print(str(arr).strip("[]").replace(",", ""))
        else:
            arr[i+1] = temp
            print(str(arr).strip("[]").replace(",", ""))
            break
        i -= 1


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
