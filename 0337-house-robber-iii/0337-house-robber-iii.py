# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return [0,0]
            left=helper(root.left)
            right=helper(root.right)
            return [root.val+left[1]+right[1],max(left)+max(right)]
        res=helper(root)
        return max(res[0],res[1])            
        