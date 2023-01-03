# Enter your code here. Read input from STDIN. Print output to STDOUT
# problem link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
from collections import defaultdict
n, m = list(map(int, input().split()))
holder_dict = defaultdict(list)
for i in range(n):
    holder_dict['A'].append(input())
for i in range(m):
    holder_dict['B'].append(input())
for i in holder_dict['B']:
    checker = []
    for j in range(len(holder_dict['A'])):
        if holder_dict['A'][j] == i:
            checker.append(str(j+1))
    if len(checker) == 0:
        print(-1)
    else:
        print(" ".join(checker))
