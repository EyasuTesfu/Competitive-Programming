
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    i = -2
    temp = arr[-1]
    while(i >= -n-1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = temp
            print(str(arr).strip("[]").replace(",", ""))
            break
        print(str(arr).strip("[]").replace(",", ""))
        i -= 1


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
