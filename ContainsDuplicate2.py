class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited={}
        #to store the element with its index
        for i, val in enumerate(nums):
            if val in visited and i-visited[val]<=k:
                return True
            else:
                visited[val]=i
        return False