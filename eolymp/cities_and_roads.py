n = int(input())
grid = [input().split() for i in range(n)]
count = 0
vis = set()
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1':
            if i != j and (i, j) not in vis:
                count += 1
                vis.add((i, j))
                vis.add((j, i))
print(count)
