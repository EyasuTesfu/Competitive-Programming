# problem link: https://codeforces.com/problemset/problem/1741/A
n = int(input())
for i in range(n):
    sizes = input().split()
    if sizes[0][-1] == sizes[1][-1]:
        a = len(sizes[0]) - 1
        b = len(sizes[1]) - 1
        if sizes[0][-1] == "S":
            if a < b:
                print(">")
            elif a == b:
                print("=")
            elif a > b:
                print("<")
        else:
            if a > b:
                print(">")
            elif a == b:
                print("=")
            elif a < b:
                print("<")
    else:
        if sizes[0][-1] == "L":
            print(">")
        elif sizes[1][-1] == "L":
            print("<")
        elif sizes[0][-1] == "M":
            print(">")
        elif sizes[1][-1] == "M":
            print("<")
