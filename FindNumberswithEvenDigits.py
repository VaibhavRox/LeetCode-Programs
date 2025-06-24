class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            digits=0
            num=i
            while num>0:
                num=num//10
                digits+=1
            if digits%2==0:
                count+=1
        return count