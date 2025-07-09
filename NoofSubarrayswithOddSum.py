class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=10**9+7
        odd,even=0,1  #to consider prefix 0 (sum befo starting)
        result,prefix=0,0
        for num in arr:
            prefix+=num #find the prefix sum always
            if prefix%2==0:
                #Even prefix sum
                result+=odd   #odd prefix before + even now= odd subarray
                even+=1
            else:
                #odd prefix sum
                result+=even   #even prefix before + odd now=odd subarray
                odd+=1
        return result%mod