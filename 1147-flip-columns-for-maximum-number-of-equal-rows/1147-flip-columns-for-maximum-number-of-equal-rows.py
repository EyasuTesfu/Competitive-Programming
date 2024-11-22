class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_matching = defaultdict(int)
        for row in matrix:
            pattern = tuple(val ^ row[0] for val in row)

            pattern_matching[pattern] += 1
        return max(pattern_matching.values())
