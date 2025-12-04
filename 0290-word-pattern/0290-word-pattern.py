class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:  
        map_p_w={}
        map_w_p={}
        words=s.split()
        if len(pattern)!= len(words):
            return False 
        for p,w in zip(pattern,words):
            if  p in map_p_w and  map_p_w[p]!= w:
                    return False
            if  w in map_w_p and map_w_p[w]!= p:
                    return False
            map_p_w[p]=w
            map_w_p[w]=p
        return True
            