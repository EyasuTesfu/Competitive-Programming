class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # create the area
        area = [['unseen' for j in range(n)] for i in range(m)]
        for r, c in guards:
            area[r][c] = 'g'
        for r, c in walls:
            area[r][c] = 'w'
        
        '''area = [[0,0],
                    [0,0], 
                    [0,0]]'''
        # simulate it
        # run horizontally from left to right and right to left
        for i in range(m):
            eyes = 0
            for j in range(n):
                if area[i][j] == 'g':
                    eyes = 1
                elif area[i][j] == 'w':
                    eyes = 0
                elif area[i][j] == 'unseen':
                    if eyes == 1:
                        area[i][j] = 'seen'
            eyes = 0

            for j in range(n-1, -1, -1):

                if area[i][j] == 'g':
                    eyes = 1
                elif area[i][j] == 'w':
                    eyes = 0
                elif area[i][j] == 'unseen':
                    if eyes == 1:
                        area[i][j] = 'seen'

        # run vertically from top to bottom and from bottom to top
        for j in range(n):
            eyes = 0
            for i in range(m):
                if area[i][j] == 'g':
                    eyes = 1
                elif area[i][j] == 'w':
                    eyes = 0
                elif area[i][j] == 'unseen':
                    if eyes == 1:
                        area[i][j] = 'seen'

            eyes = 0
            for k in range(m-1, -1, -1):
                if area[k][j] == 'g':
                    eyes = 1
                elif area[k][j] == 'w':
                    eyes = 0
                elif area[k][j] == 'unseen':
                    if eyes == 1:
                        area[k][j] = 'seen'
        print(area)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if area[i][j] == 'unseen':
                    cnt += 1
        return cnt



