class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        result=[]
        for i in range(n):
            #flip the ith character of ith string
            result.append('1' if nums[i][i]=='0' else '0')
        return ''.join(result)