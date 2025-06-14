# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:  # both trees are null
            return True
        if not p or not q: # either one of trees are null
            return False
        if p.val!=q.val:
            return False
        # use recursion
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)