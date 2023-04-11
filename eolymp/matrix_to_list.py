from collections import defaultdict
# form the grid
size = int(input())
grid = []
for i in range(size):
    grid.append(input().split())

adjacency_list = defaultdict(list)

for row in range(size):
    for col in range(size):
        if grid[row][col] == '1':
            adjacency_list[row+1].append(col+1)

for key in adjacency_list:
    print(len(adjacency_list[key]), str(
        adjacency_list[key]).strip("[]").replace(",", ""))
