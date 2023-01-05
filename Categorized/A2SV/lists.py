# problem link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    res = []
    N = int(input())
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            res.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(res)
        elif command[0] == "remove":
            res.remove(int(command[1]))
        elif command[0] == "append":
            res.append(int(command[1]))
        elif command[0] == "sort":
            res = list(sorted(res))
        elif command[0] == "pop":
            res.pop()
        elif command[0] == "reverse":
            res.reverse()
