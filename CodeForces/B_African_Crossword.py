row, col = list(map(int, input().split()))
res = []
grid = []
for _ in range(row):
    grid.append(list(input()))

rows_freq = [{} for i in range(row)]
cols_freq = [{} for i in range(col)]

for i in range(row):
    for j in range(col):
        if grid[i][j] in rows_freq[i]:
            rows_freq[i][grid[i][j]] += 1
        else:
            rows_freq[i][grid[i][j]] = 1

        if grid[i][j] in cols_freq[j]:
            cols_freq[j][grid[i][j]] += 1
        else:
            cols_freq[j][grid[i][j]] = 1
for i in range(row):
    for j in range(col):
        if rows_freq[i][grid[i][j]] == 1:
            if cols_freq[j][grid[i][j]] == 1:
                res.append(grid[i][j])
print("".join(res))
