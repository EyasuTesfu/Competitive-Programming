n = int(input())
for i in range(n):
    length , k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    i = 0
    jumped = False
    while(i < length-k):
        j = i
        while(j < i + k):
            jumped = False
            if 2*arr[j+1] <= arr[j]:
                jump
                break
            j += 1
        if j == i + k:
            count += 1
        if jumped == False:
            i += 1
    print(count)