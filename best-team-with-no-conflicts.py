class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores_ages = [(scores[i], ages[i]) for i in range(len(scores))]
        scores_ages.sort()
        dp = [scores_ages[i][0] for i in range(len(scores))]
        for i in range(len(scores)):
            for j in range(i):
                if scores_ages[j][1] > scores_ages[i][1]:
                    continue 
                dp[i] = max(dp[i], scores_ages[i][0] + dp[j])
        
        return max(dp)