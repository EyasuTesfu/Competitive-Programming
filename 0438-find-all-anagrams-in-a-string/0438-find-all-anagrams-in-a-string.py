class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_counter = Counter(p)
        s2 = Counter(s[:len(p) - 1])

#         if self.check_sub(p_counter, s2):
#                 res.append(0)
                
        i, j = 0, len(p) - 1
        while j < len(s):
            
            if s[j] in s2:
                s2[s[j]] += 1
            else:
                s2[s[j]] = 1
        
            if self.check_sub(p_counter, s2):
                res.append(i)
            
            s2[s[i]] -= 1
   
            i += 1
            j += 1
        return res
    
    
    def check_sub(self, p, s2):
        for i in p:
            if p[i] != s2.get(i, 0):
                return False
        return True
                    