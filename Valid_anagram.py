class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s)==Counter(t)
    
    # can also just sort each and then return its equality
    # t=sorted(t)
    # s=sorted(s)
    # return s==t