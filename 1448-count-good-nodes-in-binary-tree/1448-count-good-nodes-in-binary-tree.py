# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#       ++  self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def helper(root,maxval):
            nonlocal count
            if root is None:
                return 0
            if root.val >=maxval:
                count+=1
            maxval=max(root.val,maxval)
            helper(root.left,maxval)
            helper(root.right,maxval)
            
        helper(root,root.val)
        return count 
                



        