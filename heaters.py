class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        i = 0
        j = 0
        max_dist = 0
        while i < len(houses) and j < len(heaters):
            dif1 = abs(heaters[j]-houses[i])
            if j + 1 != len(heaters):
                dif2 = abs(heaters[j+1]-houses[i])
                if dif2 <= dif1:
                    j += 1
                    continue
            if dif1 > max_dist:
                max_dist = max(max_dist, dif1)
            i += 1
        return max_dist