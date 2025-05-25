class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        z=bin(x+y)[2:] #to remove the prefix 0b
        return z
        