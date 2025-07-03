class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            newstring=""
            for ch in word:
                if ch=="z":
                    newstring+="a"
                else:
                    newstring+=chr(ord(ch)+1)
            word+=newstring
        return word[k-1]