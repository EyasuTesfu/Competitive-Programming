n, m = map(int, input().split())
prefix_sum = [0]*(n+1)
for i in range(m):
    start, end = map(int, input().split())
    prefix_sum[start] += 1
    prefix_sum[end+1] -= 1
if prefix_sum[0] == 0:
    print("YES")
else:
    ans = "NO"
    for i in range(1,n):
        prefix_sum[i] += prefix_sum[i-1]
        if prefix_sum[i] == 0:
            ans = "YES"
            break
    print(ans)