# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur,val):
            if not cur:
                return 0
            val=val*10+cur.val
            if not cur.right and not cur.left:
                return val
            return dfs(cur.left,val)+dfs(cur.right,val)
        return dfs(root,val=0)
