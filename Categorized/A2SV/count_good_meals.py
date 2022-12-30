# problem link: https://leetcode.com/problems/count-good-meals/description/
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        amount = Counter(deliciousness)
        count = 0
        power = [pow(2, i) for i in range(22)]
        for i in amount:
            j = 0
            while(j < len(power)):
                if (power[j] - i) in amount and amount[power[j] - i] > 0:
                    if i == power[j] - i:
                        count += amount[i] * (amount[i] - 1)
                    else:
                        count += amount[power[j]-i] * amount[i]
                j += 1
        count = count // 2
        return (count) % (10**9 + 7)