n, k = map(int, input())
arr = list(map(int, input().split()))
# greater than the k and lower than the k + 1
arr.sort()
for i in range(len(arr)):
    if arr[i] == arr