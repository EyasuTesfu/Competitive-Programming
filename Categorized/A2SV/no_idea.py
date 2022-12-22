# problem link: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
_list = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happy = 0
for i in _list:
    if i in set_a:
        happy += 1
    if i in set_b:
        happy -= 1
print(happy)
