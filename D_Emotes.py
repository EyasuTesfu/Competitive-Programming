n, m, k = map(int, input().split())
arr = sorted(list(map(int,input().split())), reverse=True)
hap = 0
_k = k+1
if m%(_k) == 0:
    hap += k*arr[0]*(m//_k) + arr[1]*(m//_k)
elif m%(_k) != 0:
    hap += k*arr[0]*(m//_k) + arr[1]*(m//_k) + (m%_k)*arr[0]
# while m > 0:
#     if turn == 0:
#         _min = min(m, k)
#         hap += arr[0]*_min
#         turn = 1
#         m -= _min
#     elif turn == 1:
#         hap += arr[1]*1
#         turn = 0
#         m -= 1
print(hap)