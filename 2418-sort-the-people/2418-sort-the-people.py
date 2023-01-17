class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _max = max(heights)
        counter = []
        names2 = []
        for i in range(_max+1):
            counter.append(0)
        for i in range(len(heights)):
            counter[heights[i]] += 1
        for i in range(len(counter)-1, -1, -1):
            for j in range(counter[i]):
                index = heights.index(i)
                names2.append(names[index])
        return names2