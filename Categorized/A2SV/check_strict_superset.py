# problem link:https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
A = set(list(map(int, input().split())))
n = int(input())
for i in range(n):
    B = set(list(map(int, input().split())))
    if not B.issubset(A) or len(A) <= len(B):
        print(False)
        break
    if i == n - 1:
        print(True)
