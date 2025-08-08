class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        length=len(flowerbed)
        for i in range(length):
            if flowerbed[i]==0:
                #check left and right neighbours if they are 0, otherwise leave
                left_empty=(i==0) or (flowerbed[i-1]==0)
                right_empty=(i==length-1) or (flowerbed[i+1]==0)
                if left_empty and right_empty:
                    n-=1
                    flowerbed[i]=1
                    if n==0:
                        return True
        return n<=0