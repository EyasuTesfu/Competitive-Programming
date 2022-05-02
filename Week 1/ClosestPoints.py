import math


def kClosest(points, k: int):
    points.sort(key=(lambda point: point[0] ** 2 + point[1] ** 2))
    return points[:k]


print(kClosest([[0, 1], [1, 0]], 2))
print(kClosest([[1, 3], [-2, 2]], 1))
