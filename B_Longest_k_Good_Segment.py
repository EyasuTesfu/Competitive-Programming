from collections import deque
# use two pointers and a set
n, k = map(int, input().split())
nums = list(map(int, input().split()))
a_set = set()
left = 0
min_left = left
max_right = right
counter_dict = 0
queue = deque()
for right in range(n):
    a_set.add(nums[right])
    queue.append(nums[right])
    if nums[right] in counter_dict:
        counter_dict[nums[right]] += 1
    else:
        counter_dict[nums[right]] = 1
    if len(a_set) == k:
        min_left, max_right = left, right
    elif len(a_set) > k:
        if nums[queue.popleft()]