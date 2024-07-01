# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        sortedVal=inorder(root)

        def bstBuild(values):
            if not values:
                return None
            mid=len(values)//2
            root=TreeNode(values[mid])
            root.left=bstBuild(values[:mid])
            root.right=bstBuild(values[mid+1:])
            return root
        return bstBuild(sortedVal)