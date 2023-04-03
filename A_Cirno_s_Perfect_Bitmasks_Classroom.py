t = int(input())
for i in range(t):
    x = int(input())
    j = k = 0
    # j is the ones position
    while (1 << j) & x == 0:
        j += 1
    # k is the zero position
    while (1 << k) & x != 0:
        k += 1
    y = 1 << j
    if x > y:
        print(y)
    else:
        print(y + (1 << k))
