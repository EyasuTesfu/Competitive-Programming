# problem link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_dict = {}
        lose_dict = {}
        for i in matches:
            if i[0] in win_dict:
                win_dict[i[0]] += 1
            else:
                win_dict[i[0]] = 1
            if i[1] in lose_dict:
                lose_dict[i[1]] += 1
            else:
                lose_dict[i[1]] = 1
        output = []
        not_lost_match = []
        lost_exactly_one = []
        for i in win_dict:
            if i not in lose_dict:
                not_lost_match.append(i)
        for i in lose_dict:
            if lose_dict[i] == 1:
                lost_exactly_one.append(i)
        output.append(sorted(not_lost_match))
        output.append(sorted(lost_exactly_one))
        return output
