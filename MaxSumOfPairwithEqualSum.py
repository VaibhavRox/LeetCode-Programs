class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        digit_map={}
        max_sum=-1
        for num in nums:
            dsum=digit_sum(num)
            if dsum in digit_map:
                #update max_sum, if we already have a number with same digit sum
                max_sum=max(max_sum,digit_map[dsum]+num)
                #keep the larger of the two numbers
                digit_map[dsum]=max(digit_map[dsum],num)
            else:
                digit_map[dsum]=num
        return max_sum