class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        char_to_word={}
        word_to_char={}

        for ch,word in zip(pattern,words):
            #check if ch is already mapped
            if ch in char_to_word:
                #check if mapping is same
                if char_to_word[ch]!=word:
                    return False
            else:
                #check if word already mapped to some other char
                if word in word_to_char:
                    return False
                char_to_word[ch]=word
                word_to_char[word]=ch
        return True  