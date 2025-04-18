class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        rle_str = self.countAndSay(n-1) + "0"

        # RLE calculating part
        holder = ""
        final_str = []
        holder = rle_str[0]
        count = 1
        for i in range(1, len(rle_str)):
            if holder == rle_str[i]:
                count += 1
            else:
                # write on final_str
                final_str.append(str(count))
                final_str.append(holder)

                #reset holder and count
                holder = rle_str[i]
                count = 1
        
        return "".join(final_str)
        

        