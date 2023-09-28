n, k = map(int, input().split())
seq = list(map(int, input().split()))
sorted_seq = sorted(seq)
ans = -1
if k == 0:
    ans = sorted_seq[0] - 1
else:
    if k == n:
        ans = sorted_seq[k-1]
    elif sorted_seq[k] > sorted_seq[k-1]:
        if sorted_seq[k] - 1 >= sorted_seq[k-1]:
            ans = sorted_seq[k] - 1
if ans <= 0 or ans > 10**9:
    ans = -1
print(ans)