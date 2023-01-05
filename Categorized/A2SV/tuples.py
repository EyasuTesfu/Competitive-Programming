# problem link:https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
n = int(input())
t = list(map(int, input().split()))
print(hash(tuple(t)))