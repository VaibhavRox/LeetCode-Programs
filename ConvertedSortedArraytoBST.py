# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(start,end):
            if start>end:
                return None
            mid=(start+end)//2
            root=TreeNode(nums[mid])  #assume the middle element of the sorted array is root, as it splits the tree
            root.left=helper(start,mid-1)  #similarly find the root of left subtree
            root.right=helper(mid+1,end)    #find root of right subtree and recursively repeat
            return root
        return helper(0,len(nums)-1)