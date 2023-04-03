q = int(input())
for i in range(q):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    left = 0
    right = 4*n-1
    area = arr[left]*arr[right]
    ans = "YES"
    while left <= right:
        if arr[left]*arr[right] == area:
            left += 1
            right -= 1
        else:
            ans = "NO"
            break
    print(ans)