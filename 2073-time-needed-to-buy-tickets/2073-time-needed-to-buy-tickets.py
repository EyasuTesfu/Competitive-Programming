class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(k+1):
            if tickets[i] <= tickets[k]:
                time += tickets[i]
                
            elif tickets[i] > tickets[k]:
                time += tickets[k]
                
        for j in range(k+1, len(tickets)):
            if tickets[j] < tickets[k]:
                time += tickets[j]
                
            elif tickets[j] >= tickets[k]:
                time += tickets[k]-1
        return time