n, p = map(int, input().split())
arr = sorted(list(map(int, input().split())))
left = 0
right = n-1
res = 0
team_counter = 1
# use the right to go from the left
while left <= right:
    if team_counter* arr[right] > p:
        res += 1
        team_counter = 1
        right -= 1
    elif team_counter * arr[right] <= p:
        team_counter += 1
        left += 1
print(res)