class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        for i in words:
            if len(i) > max_len:
                max_len = len(i)
        output = [""]*max_len

        for word in words:
            for j in range(max_len):
                if j < len(word):
                    output[j] += word[j]
                else:
                    output[j] += " "
        output2 = []
        for lett in output:
            output2.append(lett.rstrip())
        return output2
                    