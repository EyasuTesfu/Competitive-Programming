n = int(input())
for i in range(n):
    m = int(input())
    pass_arr = sorted(list(map(int, input().split())))
    mean = sum(pass_arr)/m
    # assign the target
    target = sum(pass_arr)- mean*(m-2) 
    
    # binary search
    def binary_search(target, arr, count=0, idx=0):
        print(arr, pass_arr)
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] == target:
                count += 1
                left_count = mid-1
                right_count = mid + 1
                print(mid, "mid")
                # after mid is found check if right and left sides also contain target
                while left_count >= 0 and arr[left_count] == target:
                    print("left count", arr[left_count])
                    count += 1
                    left_count -= 1
                while right_count < len(arr) and arr[right_count] == target:
                    print("right count", right_count, count)
                    count += 1
                    right_count += 1
                return count
            elif arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
        return count
    
    #  do binary search on the 2nd item
    count = 0
    
    for i in range(m):
        count += binary_search(target-pass_arr[i], pass_arr[i+1:], count, i)
    print(count)