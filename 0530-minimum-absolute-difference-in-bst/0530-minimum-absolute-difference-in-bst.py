# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst=[]
        
        def helper(root):
            if root is None:
                return None
            if root.left:
                helper(root.left)
            lst.append(root.val)
            if root.right:
                helper(root.right)
            
        helper(root)
        minVal=float('inf')
        for i in range(1,len(lst)):
            minVal=min(minVal,lst[i]-lst[i-1])
        return minVal


            
            
       