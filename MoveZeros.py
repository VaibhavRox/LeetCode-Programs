class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero,i=0,0
        while i<len(nums):
            if nums[i]!=0:
                nums[i],nums[nonzero]=nums[nonzero],nums[i]
                nonzero+=1
            i+=1