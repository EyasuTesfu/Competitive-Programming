class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = {}
        col_dict = {}
        output = 0
        for i in range(len(grid)):
            temp = tuple(grid[i])
            if temp in row_dict:
                row_dict[temp] += 1
            else:
                row_dict[temp] = 1
        for i in range(len(grid)):
            temp = tuple([row[i] for row in grid])
            if temp in col_dict:
                col_dict[temp] += 1
            else:
                col_dict[temp] = 1
        for col in col_dict:
            if col in row_dict:
                output += col_dict[col] * row_dict[col]
        return output
            