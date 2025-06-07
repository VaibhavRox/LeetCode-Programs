class Solution:
    def reverseVowels(self, s: str) -> str:
        words=list(s)
        start=0
        end=len(words)-1
        vowels="aeiouAEIOU"
        while start<end:
            while start<end and words[start] not in vowels:
                start+=1
            while start<end and words[end] not in vowels:
                end-=1
            #swap the start and end pos
            words[start],words[end]=words[end],words[start]
            start+=1
            end-=1
        result="".join(words)
        return result
