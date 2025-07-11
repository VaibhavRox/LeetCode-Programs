class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        max_len=0
        left=0  #start of window
        for right in range(len(s)):
            #while loop shrinks the window from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len