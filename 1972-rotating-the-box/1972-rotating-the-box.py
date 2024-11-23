class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotated_box = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            last_spot = deque()
            for j in range(n-1, -1, -1):
                if box[i][j] == '*':
                    last_spot = deque()
                    rotated_box[j][m-1-i] = '*'
                if box[i][j] == '#':
                    if len(last_spot) != 0:
                        rotated_box[last_spot[0]][m-1-i] = '#'
                        last_spot.append(j)
                        rotated_box[j][m-1-i] = '.'
                        last_spot.popleft()
                    else:
                        rotated_box[j][m-1-i] = '#'
                if box[i][j] == '.':
                    last_spot.append(j)
        
        return rotated_box
