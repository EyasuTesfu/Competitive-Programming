class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            pos = i
            count = 0
            for j in range(0, pos):
                if boxes[j] == "1":
                    count += abs(j-pos)
            for k in range(pos+1, len(boxes)):
                if boxes[k] == "1":
                    count += abs(k - pos)
            res.append(count)
        return res