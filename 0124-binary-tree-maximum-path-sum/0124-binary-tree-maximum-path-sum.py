# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal=root.val
        def dfs(root):
            global maxVal
            if root is None:
                return 0
            lval,rval=0,0
            lval=max(dfs(root.left),0)
            rval=max(dfs(root.right),0)
            self.maxVal=max(root.val+lval+rval,self.maxVal)
            return max(root.val+lval,root.val+rval)
        
        dfs(root)
        return self.maxVal