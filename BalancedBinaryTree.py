# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def check(node):
            if not node: # empty tree
                return 0
            left=check(node.left)
            if left==-1:
                return -1 #left subtree not balanced
            right=check(node.right)
            if right==-1:
                return -1 #right subtree not balanced
            if abs(left-right)>1:
                return -1  #current node not balanced as difference in depth is more than 1
            return max(left,right)+1
        return check(root)!=-1