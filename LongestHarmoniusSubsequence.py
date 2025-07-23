class Solution:
    def findLHS(self, nums):
        nums.sort()
        j=0
        maxlen=0
        for i in range(0,len(nums)):
            while nums[i]-nums[j]>1:
                j+=1
            if nums[i]-nums[j]==1:
                maxlen=max(maxlen,i-j+1)
        return maxlen