class Solution:
    def groupAnagrams(self, strs):
        anagram={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(s)
        return list(anagram.values())