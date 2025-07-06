from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=defaultdict(int)
        good_pairs=0
        for i,num in enumerate(nums):
            key=num-i
            good_pairs+=count[key]
            count[key]+=1
        total_pairs=n*(n-1)//2
        return total_pairs-good_pairs