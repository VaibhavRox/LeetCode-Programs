class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums:
            return res
        start=nums[0]
        end=nums[0] 
        #Start moving end for each consecutive value, then on reaching a non-consecutive number, stop end, and append to res as that is the range
        for i in nums[1:]:
            if i==end+1:
                end=i
            else:
                if start==end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start=i
                end=i
        #For final values
        if start==end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))
        return res