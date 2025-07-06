from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count=Counter(arr)
        max_lucky=-1
        for key,value in count.items():
            if key==value:
                max_lucky=max(key,max_lucky)
        return max_lucky