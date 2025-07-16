class Solution:
    def palindromePairs(self, words):
        def isPalindrome(s):
            return s==s[::-1]
        rev_index={}
        res=[]
        for i in range(len(words)):
            rev_word=words[i][::-1]
            rev_index[rev_word]=i
        for i, word in enumerate(words):
            n=len(word)
            for k in range(n+1):  #try every possible cut position
                suff,pref=word[k:],word[:k]
                if isPalindrome(pref):
                    j=rev_index.get(suff)
                    if j is not None and j!=i:
                        res.append([j,i])
                if k!=n and isPalindrome(suff):
                    j=rev_index.get(pref)
                    if j is not None and j!=i:
                        res.append([i,j])      #as suffix is a palindrome, then word+rev(pref) is a palindrome
        return res
