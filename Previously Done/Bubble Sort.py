def countSwaps(a):
    length = len(a)
    count = 0
    for i in range(length):
        for j in range(length-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count+=1
    print("Array is sorted in %s swaps."%(count))
    print("First Element: %s"%(a[0]))
    print("Last Element: %s"%(a[length-1]))
