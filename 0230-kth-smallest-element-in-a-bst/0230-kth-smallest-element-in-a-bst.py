# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result=None
        self.count=0
        def helper(root):
            if not root or self.result is not None:
                return
            
            helper(root.left)
            self.count+=1
            if self.count==k:
                self.result=root.val
                return
            helper(root.right)
        helper(root)
        return self.result