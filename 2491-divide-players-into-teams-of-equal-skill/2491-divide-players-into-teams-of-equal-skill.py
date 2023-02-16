class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2 != 0:
            return -1
        skill.sort()
        l, r = 0, len(skill)-1
        _sum = skill[l] + skill[r]
        chemistry = skill[l] * skill[r]
        l += 1
        r -= 1
        while(l < r):
            if skill[l] + skill[r] != _sum:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        return chemistry