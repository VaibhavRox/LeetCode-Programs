class Solution:
    def runningSum(self, nums):
        s=0
        for i in range(0,len(nums)):
            s=s+nums[i]
            nums[i]=s
        return nums
            