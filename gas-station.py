class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, credit, debit = None, 0, 0

        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                start, credit, debit = None, 0, debit - credit
            elif start == None:
                start = i
            
        if credit >= debit:
            return start
        return -1