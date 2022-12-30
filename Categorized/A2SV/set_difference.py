# problem link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
size = int(input())
english = set(input().split())
size = int(input())
french = set(input().split())
print(len(english.difference(french)))
