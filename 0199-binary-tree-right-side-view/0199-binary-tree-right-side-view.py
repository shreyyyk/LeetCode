# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        queue=collections.deque([root])
        while(queue):
            rightNode= None
            qlen=len(queue)

            for i in range(qlen):
                node=queue.popleft()
                if node:
                    rightNode=node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res
