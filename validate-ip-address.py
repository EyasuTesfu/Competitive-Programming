class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dot_count = queryIP.count(".")
        if dot_count == 0:
            colon_count = queryIP.count(":")
            if colon_count == 0:
                return "Neither"
            arr = queryIP.split(":")
            if len(arr) != 8:
                return "Neither"
            for num in arr:
                if len(num) > 4 or len(num) < 1:
                    return "Neither"
                for let in num:
                    val = ord(let)
                    if 48 <= val <= 57 or 65 <= val <= 70 or 97 <= val <= 102:
                        continue
                    else:
                        return "Neither"
            return "IPv6"
                
        else:
            arr = queryIP.split(".")
            if len(arr) != 4:
                return "Neither"
            for num in arr:
                try:
                    val = int(num)
                except:
                    return "Neither"
                if not 0 <= val <= 255:
                    return "Neither"
                if num[0] == '0' and len(num) > 1:
                    return "Neither"
            
            return "IPv4"