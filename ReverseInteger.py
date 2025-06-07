class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x<0: #if number is negative, start from first digit, convert the number to string, then reverse it and convert back to int
            res=int(str(x)[1:][::-1])*-1
        else:
            res=int(str(x)[::-1]) # the [::-1] basically returns the string in reverse
        if res>2**31-1 or res<-2**31:
            return 0
        return res