# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=collections.deque([root])
        res=[]
        
        while(q):
            qlen=len(q)
            val=0
            for i in range(qlen):
                node=q.popleft()
                if node:
                    val=val+node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            avgval=val/(qlen)
            res.append(avgval)
        return res