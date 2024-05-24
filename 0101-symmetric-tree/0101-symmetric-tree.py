# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self,root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
    def isSameTree(self,p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:
            if p is None and q is None :
                return True
            if p is None or q is None:
                return False
        
            if p.val!=q.val:
                return False
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftTree=self.invertTree(root.left)
        return self.isSameTree(leftTree,root.right)
