# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0:
            return []
        def generator(n):
            if n==1:
                return [TreeNode(0)]
            trees=[]
            for leftSize in range(1,n,2):
                rightSize=n-leftSize-1
                leftTrees=generator(leftSize)
                rightTrees=generator(rightSize)
                for left in leftTrees:
                    for right in rightTrees:
                        trees.append(TreeNode(0,left,right))
            return trees
        return generator(n)