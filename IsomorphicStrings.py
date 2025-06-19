class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s_t={}
        map_t_s={}
        for c1,c2 in zip(s,t):
            if c1 in map_s_t:
                if map_s_t[c1]!=c2:
                    return False
            else:
                if c2 in map_t_s:
                    return False # prevents two s chars mapping to same t char
                map_s_t[c1]=c2
                map_t_s[c2]=c1
        return True
                