# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(node,result):
            if not node:
                return []
            helper(node.left,result)
            helper(node.right,result)
            result.append(node.val)
        result=[]
        helper(root,result)
        return result