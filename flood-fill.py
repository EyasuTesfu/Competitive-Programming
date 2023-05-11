class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        if image[sr][sc] == color:
            return image
        def dfs(prev_color, row, col):
            if image[row][col] != prev_color:
                return
            image[row][col] = color
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    dfs(prev_color, new_r,new_c)
        dfs(image[sr][sc], sr, sc)
        return image