# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid=((len(nums)+1)//2)-1
        if mid<=-1:
            return None
        left=nums[:mid]
        right=nums[mid+1:]
        cur=TreeNode(nums[mid])
        cur.left=self.sortedArrayToBST(left)
        cur.right=self.sortedArrayToBST(right)
        return cur