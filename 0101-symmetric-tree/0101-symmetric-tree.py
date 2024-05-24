# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:
        if p is None and q is None :
            return True
        if p is None or q is None:
            return False
        
        return p.val == q.val and self.isSame(p.left,q.right) and self.isSame(p.right,q.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSame(root.left,root.right)