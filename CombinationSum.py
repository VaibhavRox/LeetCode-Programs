class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start,path,total):
            if total==target:
                result.append(path[:])
                return 
            if total>target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])   #use i instead of i+1, as we can reuse it
                path.pop()
        backtrack(0,[],0)
        return result