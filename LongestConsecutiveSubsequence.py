class Solution:
    def longestConsecutive(self, nums) :
        #use a set to remove duplicates
        s=set(nums)
        longest=0
        for n in s:
            #only count if its start of a sequence
            if n-1 not in s:
                curr=n
                count=1
                while curr+1 in s:
                    curr+=1
                    count+=1
                longest=max(longest,count)
        return longest