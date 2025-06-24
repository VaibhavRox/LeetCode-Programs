class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        
        consecutive=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                consecutive.append(count)
                count=0
        consecutive.append(count)
                
        return max(consecutive)