def right_traversal(mat):
    diagonal = {}
    diagonal2 = {}
    row, col = len(mat), len(mat[0])
    for i in range(row):
        for j in range(col):
            if (i + j) in diagonal2:
                diagonal2[i+j] += int(mat[i][j])
            elif (i+j) not in diagonal2:
                diagonal2[i + j] = int(mat[i][j])
            if (j-i) in diagonal:
                diagonal[j-i] += int(mat[i][j])
            elif (j-i) not in diagonal:
                diagonal[j-i] = int(mat[i][j])

    return diagonal, diagonal2


test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(input().split())
    right_diagonal, left_diagonal = right_traversal(grid)
    max_diagonal = 0

    for i in range(n):
        for j in range(m):
            max_diagonal = max(max_diagonal, int(
                right_diagonal[j-i]+int(left_diagonal[i+j] - int(grid[i][j]))))
    print(max_diagonal)
