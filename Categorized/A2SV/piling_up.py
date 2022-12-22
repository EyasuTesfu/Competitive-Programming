# problem link:https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
t = int(input())
blocks = []
for i in range(t):
    size = input()
    blocks.append(list(map(int, input().split())))

for i in blocks:
    left = 0
    right = len(i)-1
    stack = []
    while(left <= right):
        if not stack:
            if i[right] >= i[left]:
                stack.append(i[right])
                right -= 1
            else:
                stack.append(i[left])
                left += 1
        else:
            if i[right] >= i[left]:
                stack.append(i[right])
                right -= 1
            else:
                stack.append(i[left])
                left += 1
            if stack[-1] > stack[-2]:
                break
    if len(stack) < len(i):
        print("No")
    else:
        print("Yes")
