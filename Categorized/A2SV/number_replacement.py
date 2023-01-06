# problem link: https://codeforces.com/problemset/problem/1744/A
n = int(input())
for i in range(n):
    letter_number = {}
    size = int(input())
    nums = list(map(int, input().split()))
    letters = input()
    i = 0
    while(i < size):
        if nums[i] in letter_number:
            if letter_number[nums[i]] != letters[i]:
                print("NO")
                break
        else:
            letter_number[nums[i]] = letters[i]
        i += 1
    if i == size:
        print("YES")
