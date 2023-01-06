# problem link: https://codeforces.com/problemset/problem/1730/A
from collections import Counter
n = int(input())
for i in range(n):
    size, cost = list(map(int, input().split()))
    planets = Counter(list(map(int, input().split())))
    total_cost = 0
    for i in planets:
        if cost <= planets[i]:
            total_cost += cost
        else:
            total_cost += planets[i]
    print(total_cost)
