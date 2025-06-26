# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #Binary search approach
        left,right=1,n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid  #mid might be the first bad version
            else:
                left=mid+1  #first bad version might be after mid
        return left
#isBadVersion is a predefined function that checks if a version is bad or not.