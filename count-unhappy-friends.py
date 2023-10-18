class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        count = 0
        pairings = defaultdict(int)
        for a, b in pairs:
            pairings[a] = b
            pairings[b] = a
        for a, b in pairs:
            found = False
            for pref in preferences[a]:
                if pref == b or found:
                    break
                for sec_pref in preferences[pref]:
                    if sec_pref == pairings[pref]:
                        break
                    if sec_pref == a:
                        count += 1
                        found = True
                        break
            found = False
            for pref in preferences[b]:
                if found or pref == a:
                    break
                for sec_pref in preferences[pref]:
                    if sec_pref == pairings[pref]:
                        break
                    if sec_pref == b:
                        count += 1
                        found = True
                        break
        return count