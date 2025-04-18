class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        rle_str = self.countAndSay(n-1)
        holder = ""
        final_str = []
        holder = rle_str[-1]
        count = 1
        for i in range(len(rle_str)-2, -1, -1):
            if holder == rle_str[i]:
                count += 1
            else:
                final_str.append(holder)
                final_str.append(str(count))
                holder = rle_str[i]
                count = 1
        final_str.append(holder)
        final_str.append(str(count))
        final_str = final_str[::-1]
        return "".join(final_str)
        

        