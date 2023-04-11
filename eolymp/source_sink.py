from collections import defaultdict
# form the grid
size = int(input())
grid = []
for i in range(size):
    grid.append(input().split())

# hold the sinks and the sources in the array
source = []
sink = []

# rows and cols are in the
for row in range(size):
    _sink = 0
    for col in range(size):
        if grid[row][col] == '1':
            _sink = row + 1
            break
    if _sink == 0:
        sink.append(row + 1)

for col in range(size):
    _source = 0
    for row in range(size):
        if grid[row][col] == '1':
            _source = col + 1
            break
    if _source == 0:
        source.append(col + 1)

print(len(source), str(source).strip("[]").replace(",", ""))
print(len(sink), str(sink).strip("[]").replace(",", ""))
