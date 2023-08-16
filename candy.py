class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_sum = [1 for _ in range(len(ratings))]
        if len(ratings) == 1:
            return 1
        for i in range(1, len(ratings)):
            curr = ratings[i]
            prev = ratings[i-1]
            if curr > prev:
                candy_sum[i] = candy_sum[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            curr = ratings[i]
            prev = ratings[i+1]
            if curr > prev and candy_sum[i] <= candy_sum[i+1]:
                candy_sum[i] = candy_sum[i+1] + 1
        return sum(candy_sum)