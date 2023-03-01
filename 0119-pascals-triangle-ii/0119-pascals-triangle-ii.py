class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1]
        prev_row = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            row.append(prev_row[i-1]+ prev_row[i])
        row.append(1)
        return row