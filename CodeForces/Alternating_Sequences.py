import sys
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    neg = pos = False
    if n == 1:
        print(nums[0])
    else:
        _max = nums[0]
        if nums[0] <0:
            neg = True
        else:
            pos = True
        _sum = 0
        for i in range(1,n):
            if pos == True and nums[i] > 0:
                _max = max(_max, nums[i])
            if neg == True and nums[i] < 0:
                _max = max(_max, nums[i])
            if pos == True and nums[i] < 0:
                _sum += _max
                _max = nums[i]
                pos = False
                neg = True
            if neg == True and nums[i] > 0:
                _sum += _max
                _max = nums[i]
                pos = True
                neg = False
        print(_sum+_max)