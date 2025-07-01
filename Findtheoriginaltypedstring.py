class Solution:
    def possibleStringCount(self, word: str) -> int:
        total=1
        i=0
        while i<len(word):
            j=i
            #count how many times the character repeats
            while j<len(word) and word[j]==word[i]:
                j+=1
            count=j-i
            if count>1:
                total=total+count-1 #as she may have done it ATMOST once
            i=j
        return total
        