class Solution:
    def compress(self, chars: List[str]) -> int:
        def write_size(s,size) :
            """Update size and return offset"""
            if size > 1 :
                size = str(size) 
                for c in size :
                    chars[s+1] = c
                    s+=1
                return len(size)
            else :
                return 0
            
        
        s=0
        size=0
        chars.append(" ")
        
        for f in range(len(chars)) :
            
            if chars[f]!=chars[s] :
                s+=write_size(s,size)+1
                chars[s] = chars[f]
                size=0
                
            size+=1
        
        return s 