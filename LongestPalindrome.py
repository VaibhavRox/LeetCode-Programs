from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        length=0
        odd_found=False
        #use even count charas fully, and include any one odd count
        for val in count.values():
            if val%2==0:
                length+=val
            else:
                odd_found=True
                length+=val-1
        return length+1 if odd_found else length