class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word=""
        for i in s:
            if i.isalnum():
                word=word+i.lower()
        left=0
        right=len(word)-1
        while left<right:
            if word[left]!=word[right]:
                return False
            left+=1
            right-=1
        return True