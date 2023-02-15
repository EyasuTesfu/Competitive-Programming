n = int(input())
for i in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        print("YES")
        continue
    arr.sort()
    i = 1
    while (i < len(arr)):
        if arr[i] - arr[i-1] > 1:
            print("NO")
            break
        i += 1
    if i == len(arr):
        print("YES")
