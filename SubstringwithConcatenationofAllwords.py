from collections import Counter
class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        word_len=len(words[0])
        num_words=len(words)
        total_len=word_len*num_words
        word_count=Counter(words)
        res=[]
        for i in range(len(s)-total_len+1):
            seen=[]
            for j in range(i,i+total_len,word_len):
                word=s[j:j+word_len]
                seen.append(word)     #Take the word of the same length of the words elements
            if Counter(seen)==word_count:     #check whether the elements are same
                res.append(i) 
        return res