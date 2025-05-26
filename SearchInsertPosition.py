class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        #binary search
        while (l<=r):
            mid=l+(r-l)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
