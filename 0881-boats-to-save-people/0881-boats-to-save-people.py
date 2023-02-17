class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        # 1, 2, 4, 5 6
        # 1, 2, 2, 3 3
        people.sort()
        l, r, res = 0, len(people)-1, 0
        while(l <= r):
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res