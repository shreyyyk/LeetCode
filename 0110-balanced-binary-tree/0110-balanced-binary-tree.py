# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
                
                if root is None:
                    return 0, True
                
                left,leftTruth=helper(root.left)
                right,rightTruth=helper(root.right)
                
                
               
                balanced= leftTruth and rightTruth and abs(right-left)<=1
                height=max(left,right) + 1
                return height,balanced
        height, balance=helper(root)
        return balance