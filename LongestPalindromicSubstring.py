class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==1:
            return s
        start,end=0,0
        #chose a character, expand from centre(that character), towards left and right, and check if they are same
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left+1,right-1  #for valid bounds
        for i in range(len(s)):
            lo,ro=expand(i,i)  #for odd length words 
            le,re=expand(i,i+1)  #even length words
            if ro-lo>end-start:
                start,end=lo,ro
            if re-le>end-start:
                start,end=le,re
        return s[start:end+1]