class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 1
        zero_count = 0
        AB = "AB" in s
        CD = "CD" in s
        string = [l for l in s]
        
        while (AB or CD) and zero_count <= n -2:
            l = 0
            r = 1
            temp_AB = False
            temp_CD = False
            while r < n:
                if string[l] == 0:
                    l = r
                    r += 1

                elif string[r] == 0:
                    r += 1
                else:
                    if string[l] == "A" and string[r] == "B":
                        temp_AB = True
                        string[l] = 0
                        string[r] = 0
                        zero_count += 2
                    elif string[l] == "C" and string[r] == "D":
                        temp_CD = True
                        string[l] = 0
                        string[r] = 0
                        zero_count += 2
                    l = r
                    r += 1
            AB = temp_AB
            CD = temp_CD
        return len(string) - zero_count
        
                    

