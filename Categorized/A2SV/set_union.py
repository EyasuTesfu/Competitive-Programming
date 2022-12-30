# problem link: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
size = input()
english = set(input().split())
size = input()
french = set(input().split())
print(len(english.union(french)))
