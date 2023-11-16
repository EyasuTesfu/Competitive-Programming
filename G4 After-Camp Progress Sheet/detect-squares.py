class DetectSquares:

    def __init__(self):
        self.location = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.location[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x1 = point[0]
        y1 = point[1]
        res = 0
        for x, y in self.location:
            x_dist = abs(x1 - x)
            y_dist = abs(y1 - y)
            if x_dist == y_dist and x_dist > 0:
                location_1 = (x1, y)
                location_2 = (x, y1)
                if location_1 in self.location and location_2 in self.location:
                    res += self.location[(x, y)] * self.location[(x1, y)] * self.location[(x, y1)]
        return res

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)