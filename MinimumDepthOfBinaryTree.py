# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if not root:  #empty tree
            return 0 
        if not root.left:  #if left child empty, then follow non empty child path, and return it
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1