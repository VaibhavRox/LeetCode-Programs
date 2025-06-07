class Solution:
    def myAtoi(self, s: str) -> int:
        idx=0
        sign=1
        res=0
        while idx<len(s) and (s[idx]==' '): #ignore whitespaces
            idx+=1
        if (idx<len(s) and (s[idx]=='-' or s[idx]=='+')):
            if(s[idx]=='-'):
                sign=-1
            idx+=1
        while idx<len(s) and '0'<=s[idx]<='9':
            res=res*10+int(s[idx])
            #Handle overflow and underflow condition
            if res>(2**31-1):
                return sign*(2**31-1) if sign==1 else  -2**31
            idx+=1
        return res*sign