class Solution:
    def findContentChildren(self, g,s):
        #g is the greed factor of children, s is the size of cookies
        g.sort()
        s.sort()
        child,cookie=0,0
        while child<len(g) and cookie<len(s):
            if s[cookie]>=g[child]:
                child+=1
            cookie+=1
        return child