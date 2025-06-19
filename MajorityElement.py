from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        count=Counter(nums)
        n=len(nums)
        for num,freq in count.items():
            if freq > n//2:
                return num

