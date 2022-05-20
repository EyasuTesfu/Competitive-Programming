import math


def flagStones(n: int, m: int, a: int) -> int:
    width = height = 0
    if m <= a:
        width = 1
    else:
        width = math.ceil(m/a)
    if n <= a:
        height = 1
    else:
        height = math.ceil(n/a)

    return width*height


n, m, a = map(int, input().split())
print(flagStones(n, m, a))
