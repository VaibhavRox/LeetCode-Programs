class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            bit=(n>>i)&1    #get first bit of n and put in 31st bit of res, and keep doin that
            res=res|(bit<<(31-i))
        return res