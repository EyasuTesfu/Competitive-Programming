class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_drop = sorted(trips, key = lambda x: x[2])
        trips = sorted(trips, key = lambda x: x[1])
        start, end = trips[0][1], trips_drop[-1][2]
        prefix_sum = 0
        p1, p2 = 0,0
        for i in range(start, end):
            while p1 < len(trips) and trips[p1][1] == i:
                prefix_sum += trips[p1][0]
                p1 += 1
            while p2 < len(trips) and trips_drop[p2][2] == i:
                prefix_sum -= trips_drop[p2][0]
                p2 += 1
            if prefix_sum > capacity:
                return False
        return True